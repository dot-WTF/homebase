from mongoengine import Document, StringField, DateTimeField, EmailField
from src.database.connection.constants import CollectionNames
from datetime import datetime, timezone

class StudentOrganizationMongoModel(Document):
    id = StringField(primary_key=True, required=True, unique=True)
    organization_name = StringField(unique=True, required=True)
    organization_email = EmailField(required=True, unique=True)
    sns_topic_arn = StringField(required=True, unique=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))

    meta = {
        'collection' : CollectionNames.ORGANIZATIONS,
        'auto_create_index': False
    }

