from pydantic import BaseModel, EmailStr
from datetime import datetime

class CreateStudentOrganizationEventRequest(BaseModel):
    organization_abbreviation: str
    event_name: str
    event_description: str
    event_location: str
    event_datetime: datetime

class CreateStudentOrganizationEventResponse(BaseModel):
    message: str
    event_id: str

class SubscribeToStudentOrganizationEventRequest(BaseModel):
    name: str
    phone_number: str
    organization_abbreviation: str

class SubscribeToStudentOrganizationEventResponse(BaseModel):
    message: str
    sns_topic_arn: str

class CreateStudentOrganizationRequest(BaseModel):
    organization_abbreviation: str
    organization_email: EmailStr

class CreateStudentOrganizationResponse(BaseModel):
    message: str
    sns_topic_arn: str
    