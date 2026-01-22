from starlette import status
import requests

from src.agent.schema import HouseActionsSchema
from src.config.env import HOUSE_ID, RESOURCE_URL

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
        # Gracefully handle request errors
        print(f"Error sending request: \n{e}")
        return False