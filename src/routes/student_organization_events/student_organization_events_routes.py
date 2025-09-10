from src.schemas.student_organization_events.student_organization_events_schemas import (
    CreateStudentOrganizationEventResponse, SubscribeToStudentOrganizationEventResponse,
    CreateStudentOrganizationEventRequest, SubscribeToStudentOrganizationEventRequest,
    CreateStudentOrganizationRequest, CreateStudentOrganizationResponse
    )
from src.repository.student_organization_events.student_organization_input import CreateStudentOrganizationInput
from src.repository.student_organization_events.student_organization_mongo_repository  import StudentOrganizationMongoRepository
from src.messages.student_organization_events.senders import (
    create_organization_topic, publish_organization_event_notification, 
    subscribe_user_to_event, build_event_message
    )
from src.messages.student_organization_events.utils import calculate_hours_before_event
from src.messages.student_organization_events.constants import OrganizationNames
from src.schemas.student_organization_events.constants import ResponseMessages
from src.routes.student_organization_events.constants import FIRST_NOTIFICATION_HOURS, SECOND_NOTIFICATION_HOURS
from src.utils.id_generator.generator import IdGenerator
from src.utils.id_generator.constants import STUDENT_ORGANIZATION_EVENT_PREFIX
from src.database.connection.constants import MONGO_URI, MONGO_DATABASE_NAME, CollectionNames
from src.messages.student_organization_events.payload_models import EventNotificationPayload
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from starlette import status
from datetime import datetime, timezone, timedelta  

jobstores = {
    'default': MongoDBJobStore(database=MONGO_DATABASE_NAME, collection=CollectionNames.SCHEDULES, host=MONGO_URI)
}

scheduler = BackgroundScheduler(jobstores=jobstores)
scheduler.start()

router = APIRouter(prefix="/student-organization-events", tags=["Student Organization Events"])

@router.post("/create-student-organization",
             response_model=CreateStudentOrganizationResponse,
             description="Create a new student organization",
             status_code=status.HTTP_201_CREATED
            )
def create_student_organization(request: CreateStudentOrganizationRequest) -> CreateStudentOrganizationResponse:
    organization_id = request.organization_abbreviation
    organization_name = OrganizationNames[request.organization_abbreviation]
    sns_topic_arn = create_organization_topic(organization_id)
    organization_email = request.organization_email
    input_data = CreateStudentOrganizationInput(
        id=organization_id,
        organization_email=organization_email,
        organization_name=organization_name,
        sns_topic_arn=sns_topic_arn,
        created_at=datetime.now(timezone.utc).isoformat()
    )
    repository = StudentOrganizationMongoRepository()
    repository.create(input_data)

    return CreateStudentOrganizationResponse(
        message=ResponseMessages.CREATE_ORGANIZATION_SUCCESS,
        sns_topic_arn=sns_topic_arn
    )

@router.post("/create-event",
            response_model=CreateStudentOrganizationEventResponse,
            description="Create a new event for a student organization",
            status_code=status.HTTP_201_CREATED
            )
def create_event(request: CreateStudentOrganizationEventRequest) -> CreateStudentOrganizationEventResponse:
    job_id = IdGenerator(prefix=STUDENT_ORGANIZATION_EVENT_PREFIX).generate_id()
    organization_name = OrganizationNames[request.organization_abbreviation]
    event_name = request.event_name
    event_date = request.event_datetime.date().isoformat()
    event_time = request.event_datetime.time().isoformat()
    event_location = request.event_location
    event_description = request.event_description

    event_details = EventNotificationPayload(
        organization_name=organization_name,
        event_name=event_name,
        event_description=event_description,
        event_location=event_location,
        event_date=event_date,
        event_time=event_time
    )

    message = build_event_message(event_details)
    hours_before_event = calculate_hours_before_event(request.event_datetime)

    if hours_before_event < FIRST_NOTIFICATION_HOURS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Event must be created at least {FIRST_NOTIFICATION_HOURS} hours before the event start time."
        )
    
    first_notification_time = hours_before_event - FIRST_NOTIFICATION_HOURS
    second_notification_time = hours_before_event - SECOND_NOTIFICATION_HOURS

    scheduler.add_job(
        func=publish_organization_event_notification,
        args=[message, organization_name],
        trigger='date',
        next_run_time=first_notification_time,
        id=job_id,
        replace_existing=True
    )

    scheduler.add_job(
        func=publish_organization_event_notification,
        args=[message, organization_name],
        trigger='date',
        next_run_time=second_notification_time,
        id=job_id,
        replace_existing=True
    )

    return CreateStudentOrganizationEventResponse(
        message=ResponseMessages.CREATE_EVENT_SUCCESS,
        event_id=job_id
    )

@router.post("/subscribe-to-organization",
            response_model=SubscribeToStudentOrganizationEventResponse,
            description="Subscribe to a student organization event",
            status_code=status.HTTP_201_CREATED
            )
def subscribe(request: SubscribeToStudentOrganizationEventRequest) -> SubscribeToStudentOrganizationEventResponse:
    user_phone_number = request.phone_number
    organization_abbreviation = request.organization_abbreviation
    repository = StudentOrganizationMongoRepository()
    sns_topic_arn = repository.get(organization_abbreviation).sns_topic_arn
    subscribe_user_to_event(sns_topic_arn, user_phone_number)

    return SubscribeToStudentOrganizationEventResponse(
        message=ResponseMessages.SUBSCRIBE_EVENT_SUCCESS,
        sns_topic_arn=sns_topic_arn
    )