from langchain.tools import tool 
from enum import StrEnum
from src.utils.net import send_request
from src.agent.schema import (
    ToggleAlarmSchema, ToggleLightSchema, ToggleDoorSchema,
    ToggleDoorLockSchema, ToggleFanSchema, 
    SetLightSchema, SetDoorOpenSchema, SetDoorLockSchema,
    SetThermostatSchema, SetAlarmSchema, SetBlindsSchema, SetFanSchema
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

# Door control tools 
@tool(ToolNames.TOGGLE_DOOR, description=HouseActionsPrompts.TOGGLE_DOOR, args_schema=ToggleDoorSchema)
def toggle_door(action: str = "toggleDoor"):
    request = ToggleDoorSchema(action=action)
    result = send_request(request)
    return "Door toggled." if result else "Failed to toggle door."

@tool(ToolNames.SET_DOOR_OPEN, description=HouseActionsPrompts.SET_DOOR_OPEN, args_schema=SetDoorOpenSchema)
def set_door_open(open: bool, action: str = "setDoorOpen"):
    request = SetDoorOpenSchema(open=open, action=action)
    result = send_request(request)
    return "Door set open." if result else "Failed to set door open."

@tool(ToolNames.TOGGLE_DOOR_LOCK, description=HouseActionsPrompts.TOGGLE_DOOR_LOCK, args_schema=ToggleDoorLockSchema)
def toggle_door_lock(action: str = "toggleLock"):
    request = ToggleDoorLockSchema(action=action)
    result = send_request(request)
    return "Door lock toggled." if result else "Failed to toggle door lock."

@tool(ToolNames.SET_DOOR_LOCK, description=HouseActionsPrompts.SET_DOOR_LOCK, args_schema=SetDoorLockSchema)
def set_door_lock(locked: bool, action: str = "setLock"):
    request = SetDoorLockSchema(locked=locked, action=action)
    result = send_request(request)
    return "Door lock set." if result else "Failed to set door lock."

# Blinds control tools 
@tool(ToolNames.SET_BLINDS, description=HouseActionsPrompts.SET_BLINDS, args_schema=SetBlindsSchema)
def set_blinds(room:str, percentage: int, action: str = "setBlinds"):
    request = SetBlindsSchema(room=room, percentage=percentage, action=action)
    result = send_request(request)
    return "Blinds set." if result else "Failed to set blinds."

# Thermostat control tools
@tool(ToolNames.SET_THERMOSTAT, description=HouseActionsPrompts.SET_THERMOSTAT, args_schema=SetThermostatSchema)
def set_thermostat(target: int,  mode: str, action: str = "setThermostat"):
    request = SetThermostatSchema(target=target, mode=mode, action=action)
    result = send_request(request)
    return "Thermostat set." if result else "Failed to set thermostat."

# Fans control tools 
@tool(ToolNames.TOGGLE_FAN, description=HouseActionsPrompts.TOGGLE_FAN, args_schema=ToggleFanSchema)
def toggle_fan(action: str = "toggleFan"):
    request = ToggleFanSchema(action=action)
    result = send_request(request)
    return "Fan toggled." if result else "Failed to toggle fan."

@tool(ToolNames.SET_FAN, description=HouseActionsPrompts.SET_FAN, args_schema=SetFanSchema)
def set_fan(room: str, on: bool, action: str = "setFan"):  
    request = SetFanSchema(room=room, on=on, action=action)
    result = send_request(request)
    return "Fan set." if result else "Failed to set fan."

# Alarm control tools
@tool(ToolNames.TOGGLE_ALARM, description=HouseActionsPrompts.TOGGLE_ALARM, args_schema=ToggleAlarmSchema)
def toggle_alarm(action: str = "toggleAlarm"):
    request = ToggleAlarmSchema(action=action)
    result = send_request(request)
    return "Alarm toggled." if result else "Failed to toggle alarm."

@tool(ToolNames.SET_ALARM, description=HouseActionsPrompts.SET_ALARM, args_schema=SetAlarmSchema)
def set_alarm(on: bool, action: str = "setAlarm"):    
    request = SetAlarmSchema(on=on, action=action)
    result = send_request(request)
    return "Alarm set." if result else "Failed to set alarm."

HOUSE_AGENT_TOOLS = [
    toggle_light,
    set_light,
    toggle_door,
    set_door_open,
    toggle_door_lock,
    set_door_lock,
    set_thermostat,
    toggle_alarm,
    set_alarm,
    set_blinds,
    toggle_fan,
    set_fan
]