from pydantic import BaseModel

class EventNotificationPayload(BaseModel):
    organization_name: str
    event_name: str
    event_date: dict
    event_time: dict
    event_location: str
    event_description: str