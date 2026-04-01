from pydantic import BaseModel, EmailStr

class SendEmailPayload(BaseModel):
    from_address: EmailStr
    to_address: EmailStr
    subject: str
    content: str
