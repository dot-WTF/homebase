from src.messages.student_organization_events.utils import get_organization_full_name
from src.messages.student_organization_events.message_templates import EventMessages
from src.messages.student_organization_events.payload_models import EventNotificationPayload
from src.repository.student_organization_events.student_organization_mongo_repository import StudentOrganizationMongoRepository
from src.pubsub.connection.session import sns_client
    
def create_organization_topic(organization_abbreviation: str):
    response = sns_client.create_topic(Name=organization_abbreviation)
    return response.get("TopicArn")

def build_event_message(event_details: EventNotificationPayload):
    message = EventMessages.REMINDER.format(
            organization_name=event_details.organization_name,
            event_name=event_details.event_name,
            event_location=event_details.event_location,
            event_date=event_details.event_date,
            event_time=event_details.event_time,
        )
    return message

def publish_organization_event_notification(message: str, organization_name: str):
    sns_topic_arn = StudentOrganizationMongoRepository.get(organization_name).sns_topic_arn
    sns_client.publish(TopicArn=sns_topic_arn, Message=message)

def subscribe_user_to_event(topic_arn: str, user_phone_number: str):
    sns_client.subscribe(TopicArn=topic_arn, Protocol="sms", Endpoint=user_phone_number)