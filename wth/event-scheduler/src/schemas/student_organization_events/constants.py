from enum import StrEnum

class ResponseMessages(StrEnum):
    CREATE_EVENT_SUCCESS = "Student organization event created successfully."
    DELETE_EVENT_SUCCESS = "Student organization event deleted successfully."
    SUBSCRIBE_EVENT_SUCCESS = "Successfully subscribed to the student organization event."
    CREATE_ORGANIZATION_SUCCESS = "Student organization created successfully."