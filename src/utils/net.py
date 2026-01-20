from starlette import status
import requests
import os 

from src.agent.schema import HouseActionsSchema

HOUSE_ID = os.getenv("HOUSE_ID")
assert HOUSE_ID is not None, "Your HOUSE_ID environment variable is not set."

RESOURCE_URL = os.getenv("RESOURCE_URL")
assert RESOURCE_URL is not None, "Your RESOURCE_URL environment variable is not set."

def setup_headers() -> dict:

    headers = {
        "X-House-Id": HOUSE_ID,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    return headers

def send_request( data: HouseActionsSchema) -> bool:
    headers = setup_headers()

    try:
        request = {
            "action": data.action,
            "params": data.model_dump(exclude={"action"})
        }
        response = requests.post(RESOURCE_URL, headers=headers, json=request)
        return response.status_code == status.HTTP_200_OK
    except requests.RequestException as e:
        print(f"Error sending request: {e}")
        return False