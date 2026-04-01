from typing import TypeVar, Optional, Type, Union
from mongoengine import Document
from src.repository.student_organization_events.student_organization_input import CreateStudentOrganizationInput


T = TypeVar('T', bound=Document)

class CommonMongoRepository:
    def __init__(self, model_class: Type[T]):
        self.model_class = model_class

    def get(self, id: str) -> Optional[T]:
        return self.model_class.objects(id=id).first()

    def create(self, input: Union[CreateStudentOrganizationInput]) -> T:
        if self.model_class.objects(organization_name=input.organization_name).first():
            raise ValueError(f"An instance with organization_name {input.organization_name} already exists.")

        if hasattr(input, 'sns_topic_arn') and self.model_class.objects(sns_topic_arn=input.sns_topic_arn).first():
            raise ValueError(f"An instance with sns_topic_arn {input.sns_topic_arn} already exists.")
            
        return self.model_class(**input.model_dump()).save()
    