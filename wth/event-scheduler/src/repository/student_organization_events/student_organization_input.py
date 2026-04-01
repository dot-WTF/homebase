from pydantic import BaseModel, EmailStr

class CreateStudentOrganizationInput(BaseModel):
    id: str
    organization_email: EmailStr
    organization_name: str
    sns_topic_arn: str
    created_at: str
    