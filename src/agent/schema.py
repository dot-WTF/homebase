from pydantic import BaseModel, Field
from typing import Literal
from enum import StrEnum

class Rooms(StrEnum):
    LIVING_ROOM = "living"
    KITCHEN = "kitchen"
    OFFICE = "office"
    BEDROOM = "bedroom"
    OUTDOOR = "outdoor"

class ActionNames(StrEnum):
    TOGGLE_LIGHT = "toggleLight"
    SET_LIGHT = "setLight"
    TOGGLE_DOOR = "toggleDoor"
    SET_DOOR_OPEN = "setDoorOpen"
    TOGGLE_DOOR_LOCK = "toggleDoorLock"
    SET_DOOR_LOCK = "setDoorLock"
    SET_THERMOSTAT = "setThermostat"
    TOGGLE_ALARM = "toggleAlarm"
    SET_ALARM = "setAlarm"
    SET_BLINDS = "setBlinds"
    TOGGLE_FAN = "toggleFan"
    SET_FAN = "setFan"

class ThermostatMode(StrEnum):
    HEATING = "heating"
    COOLING = "cooling"
    OFF = "off"

# Base schema for house actions
class HouseActionsSchema(BaseModel):
    action: str = Field(..., description="The action to be performed in the house")

# Lights schema
valid_rooms_for_lights = Literal[
    Rooms.LIVING_ROOM,
    Rooms.KITCHEN,
    Rooms.OFFICE,
    Rooms.BEDROOM,
    Rooms.OUTDOOR
]

class ToggleLightSchema(HouseActionsSchema):
    action: Literal[ActionNames.TOGGLE_LIGHT] = Field(..., description="Action to toggle the light")
    room: valid_rooms_for_lights = Field(..., description="Room where the light is located")

class SetLightSchema(HouseActionsSchema):
    action: Literal[ActionNames.SET_LIGHT] = Field(..., description="Action to set the light")
    room: valid_rooms_for_lights = Field(..., description="Room where the light is located")
    isOn: bool = Field(..., description="Desired state of the light: True for ON, False for OFF")

# Door schema
class ToggleDoorSchema(HouseActionsSchema):
    action: Literal[ActionNames.TOGGLE_DOOR] = Field(..., description="Action to toggle the door")

class ToggleDoorLockSchema(HouseActionsSchema):
    action: Literal[ActionNames.TOGGLE_DOOR_LOCK] = Field(..., description="Action to toggle the door lock")

class SetDoorOpenSchema(HouseActionsSchema):
    action: Literal[ActionNames.SET_DOOR_OPEN] = Field(..., description="Action to set the door open")
    isOpen: bool = Field(..., description="Desired state of the door: True for OPEN, False for CLOSED")

class SetDoorLockSchema(HouseActionsSchema):
    action: Literal[ActionNames.SET_DOOR_LOCK] = Field(..., description="Action to set the door lock")
    isLocked: bool = Field(..., description="Desired state of the door lock: True for LOCKED, False for UNLOCKED")

# Thermostat schema
class SetThermostatSchema(HouseActionsSchema):
    action: Literal[ActionNames.SET_THERMOSTAT] = Field(..., description="Action to set the thermostat")
    target: int = Field(..., description="Desired temperature setting for the thermostat")
    mode: Literal["heating", "cooling", "off"] = Field(..., description="Desired mode for the thermostat")

# Alarm schema
class ToggleAlarmSchema(HouseActionsSchema):
    action: Literal[ActionNames.TOGGLE_ALARM] = Field(..., description="Action to toggle the alarm")

class SetAlarmSchema(HouseActionsSchema):
    action: Literal[ActionNames.SET_ALARM] = Field(..., description="Action to set the alarm")
    isArmed: bool = Field(..., description="Desired state of the alarm: True for ARMED, False for DISARMED")

# Blinds schema
valid_rooms_for_blinds = Literal[
    Rooms.LIVING_ROOM,
    Rooms.BEDROOM
]

class SetBlindsSchema(HouseActionsSchema):
    action: Literal[ActionNames.SET_BLINDS] = Field(..., description="Action to set the blinds")
    room: valid_rooms_for_blinds = Field(..., description="Room where the blinds are located")
    percentage: int = Field(..., description="Desired percentage of blinds open (0-100)")

# Fan schema
valid_rooms_for_fans = Literal[
    Rooms.LIVING_ROOM,
    Rooms.BEDROOM
]

class ToggleFanSchema(HouseActionsSchema):
    action: Literal[ActionNames.TOGGLE_FAN] = Field(..., description="Action to toggle the fan")
    room: valid_rooms_for_fans = Field(..., description="Room where the fan is located")

class SetFanSchema(HouseActionsSchema):
    action: Literal[ActionNames.SET_FAN] = Field(..., description="Action to set the fan")
    room: valid_rooms_for_fans = Field(..., description="Room where the fan is located")
    isOn: bool = Field(..., description="Desired state of the fan: True for ON, False for OFF")