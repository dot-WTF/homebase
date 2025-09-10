import boto3
from src.messages.student_organization_events.constants import OrganizationNames
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

def calculate_hours_before_event(event_datetime: datetime) -> int:
    if event_datetime.tzinfo is None:
        event_datetime = event_datetime.replace(tzinfo=timezone.utc)

    now = datetime.now(timezone.utc)
    hours_before = (event_datetime - now).total_seconds() / 3600
    return max(0, int(hours_before))

def get_organization_full_name(abbreviation: str) -> str:
    try:
        return OrganizationNames[abbreviation].value
    except KeyError:
        raise ValueError(f"Unknown organization abbreviation: {abbreviation}")

