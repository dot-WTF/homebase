from src.repository.common.common_mongo_repository import CommonMongoRepository
from src.models.student_organization_events.student_organization_mongo_model import StudentOrganizationMongoModel

class StudentOrganizationMongoRepository(CommonMongoRepository):
    def __init__(self):
        super().__init__(StudentOrganizationMongoModel)