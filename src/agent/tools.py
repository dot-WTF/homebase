from langchain.tools import tool 

from src.utils.net import send_request
from src.agent.schema import (
    ToggleAlarmSchema, ToggleLightSchema, ToggleDoorSchema,
    ToggleDoorLockSchema, ToggleFanSchema, 
    SetLightSchema, SetDoorOpenSchema, SetDoorLockSchema,
    SetThermostatSchema, SetAlarmSchema, SetBlindsSchema, SetFanSchema
)
from src.agent.prompts import HouseActionsPrompts

# Lights control tools
@tool
def toggle_light():
    send_request() 

@tool
def set_light():
    send_request() 

# Door control tools 
@tool
def toggle_door():
    send_request()

@tool
def set_door_open():
    send_request()

@tool
def toggle_door_lock():
    send_request()

@tool
def set_door_lock():
    send_request()

# Blinds control tools 
@tool
def set_blinds():
    send_request()

# Thermostat control tools
@tool
def set_thermostat():
    send_request()

# Fans control tools 
@tool
def toggle_fan():
    send_request()

@tool
def set_fan():  
    send_request()

# Alarm control tools
@tool
def toggle_alarm():
    send_request()

@tool
def set_alarm():    
    send_request()


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