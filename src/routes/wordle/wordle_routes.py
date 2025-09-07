from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from starlette import status
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from src.utils.id_generator.generator import IdGenerator
from src.utils.id_generator.constants import WORDLE_TASK_PREFIX
from src.routes.wordle.constants import WORDLE_REMINDER_INTERVAL_IN_HOURS
from datetime import datetime, timedelta
from src.schemas.wordle.constants import ResponseMessages
from src.schemas.wordle.wordle_schemas import CreateWordleReminderRequest, DeleteWordleReminderRequest, CreateWordleReminderResponse, DeleteWordleReminderResponse
from src.database.connection.constants import MONGO_URI, MONGO_DATABASE_NAME, CollectionNames
from src.messages.wordle.senders import send_reminder_via_gmail

jobstores = {
    'default': MongoDBJobStore(database=MONGO_DATABASE_NAME, collection=CollectionNames.SCHEDULES, host=MONGO_URI)
}

scheduler = BackgroundScheduler(jobstores=jobstores)
scheduler.start()

router = APIRouter(prefix="/wordle", tags=["Wordle"])

@router.post("/create-schedule",
            description="create a scheduled reminder for a user to play wordle",
            status_code=status.HTTP_201_CREATED,
            response_model=CreateWordleReminderResponse)
def create_schedule(request: CreateWordleReminderRequest):

    user_id = request.id
    user_name = request.name
    user_email = request.email

    job_id = IdGenerator.generate_id(WORDLE_TASK_PREFIX, user_id)

    if scheduler.get_job(job_id):
        scheduler.remove_job(job_id)

    next_run_time = datetime.now() + timedelta(hours=WORDLE_REMINDER_INTERVAL_IN_HOURS)
    scheduler.add_job(
        func=send_reminder_via_gmail,
        args=[user_email, user_name],
        trigger='interval',
        hours=WORDLE_REMINDER_INTERVAL_IN_HOURS,
        next_run_time=next_run_time,
        id=job_id,
        replace_existing=True
    )
    return CreateWordleReminderResponse(message=ResponseMessages.CREATE_SCHEDULE_SUCCESS)

@router.post("/delete-schedule",
            description="Delete a scheduled reminder for a user to play wordle",
            status_code=status.HTTP_200_OK,
            response_model=DeleteWordleReminderResponse)
def delete_schedule(request: DeleteWordleReminderRequest):
    
    user_id = request.id
    job_id = IdGenerator.generate_id(WORDLE_TASK_PREFIX, user_id)

    if not scheduler.get_job(job_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No schedule found for this user")
    
    scheduler.remove_job(job_id)
    return DeleteWordleReminderResponse(message=ResponseMessages.DELETE_SCHEDULE_SUCCESS)
