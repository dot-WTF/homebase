from langchain.tools import tool 
from enum import StrEnum
from src.utils.net import send_request
from src.agent.schema import (
    ToggleLightSchema, SetLightSchema
)
from src.agent.prompts import HouseActionsPrompts

class ToolNames(StrEnum):
    TOGGLE_LIGHT = "toggle_light"
    SET_LIGHT = "set_light"
    TOGGLE_DOOR = "toggle_door"
    SET_DOOR_OPEN = "set_door_open"
    TOGGLE_DOOR_LOCK = "toggle_door_lock"
    SET_DOOR_LOCK = "set_door_lock"
    SET_THERMOSTAT = "set_thermostat"
    TOGGLE_ALARM = "toggle_alarm"
    SET_ALARM = "set_alarm"
    SET_BLINDS = "set_blinds"
    TOGGLE_FAN = "toggle_fan"
    SET_FAN = "set_fan"

# Lights control tools
@tool(ToolNames.TOGGLE_LIGHT, description=HouseActionsPrompts.TOGGLE_LIGHT, args_schema=ToggleLightSchema)
def toggle_light(room: str, action: str = "toggleLight"):
    request = ToggleLightSchema(room=room, action=action)
    result = send_request(request) 
    return "Light toggled." if result else "Failed to toggle light."

@tool(ToolNames.SET_LIGHT, description=HouseActionsPrompts.SET_LIGHT, args_schema=SetLightSchema)
def set_light(room: str, on: bool, action: str = "setLight"):
    request = SetLightSchema(room=room, on=on, action=action)
    result = send_request(request) 
    return "Light set." if result else "Failed to set light."

HOUSE_AGENT_TOOLS = [
    toggle_light,
    set_light,
]