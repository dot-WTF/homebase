from pydantic import BaseModel, EmailStr

class CreateWordleReminderRequest(BaseModel):
    id: str
    email: EmailStr
    name: str
    interval: int 
    
class CreateWordleReminderResponse(BaseModel):
    message: str

class DeleteWordleReminderRequest(BaseModel):
    id: str

class DeleteWordleReminderResponse(BaseModel):
    message: str