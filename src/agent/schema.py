from pydantic import BaseModel, Field
from typing import Literal
from enum import StrEnum

class Rooms(StrEnum):
    LIVING_ROOM = "living"
    KITCHEN = "kitchen"
    OFFICE = "office"
    BEDROOM = "bedroom"
    OUTDOOR = "outdoor"

class ThermostatMode(StrEnum):
    HEATING = "heating"
    COOLING = "cooling"
    OFF = "off"

# Base schema for house actions
class HouseActionsSchema(BaseModel):
    action: str = Field(..., description="The action to be performed in the house")

# Lights schema
class ToggleLightSchema(HouseActionsSchema):
    action: str = Literal["toggleLight"]
    room: str = Field(..., description="Room where the light is located")

class SetLightSchema(HouseActionsSchema):
    action: str = Literal["setLight"]
    room: str = Field(..., description="Room where the light is located")
    isOn: bool = Field(..., description="Desired state of the light: True for ON, False for OFF")

# Door schema
class ToggleDoorSchema(HouseActionsSchema):
    action: str = Literal["toggleDoor"]

class ToggleDoorLockSchema(HouseActionsSchema):
    action: str = Literal["toggleDoorLock"]

class SetDoorOpenSchema(HouseActionsSchema):
    action: str = Literal["setDoorOpen"]
    isOpen: bool = Field(..., description="Desired state of the door: True for OPEN, False for CLOSED")

class SetDoorLockSchema(HouseActionsSchema):
    action: str = Literal["setDoorLock"]
    isLocked: bool = Field(..., description="Desired state of the door lock: True for LOCKED, False for UNLOCKED")

# Thermostat schema
class SetThermostatSchema(HouseActionsSchema):
    action: str = Literal["setThermostat"]
    target: int = Field(..., description="Desired temperature setting for the thermostat")
    mode: str = Field(..., description="Desired mode for the thermostat")

# Alarm schema
class ToggleAlarmSchema(HouseActionsSchema):
    action: str = Literal["toggleAlarm"]

class SetAlarmSchema(HouseActionsSchema):
    action: str = Literal["setAlarm"]
    isArmed: bool = Field(..., description="Desired state of the alarm: True for ARMED, False for DISARMED")

# Blinds schema
class SetBlindsSchema(HouseActionsSchema):
    action: str = Literal["setBlinds"]
    room: str = Field(..., description="Room where the blinds are located")
    percentage: int = Field(..., description="Desired percentage of blinds open (0-100)")

# Fan schema
class ToggleFanSchema(HouseActionsSchema):
    action: str = Literal["toggleFan"]

class SetFanSchema(HouseActionsSchema):
    action: str = Literal["setFan"]
    room: str = Field(..., description="Room where the fan is located")
    isOn: bool = Field(..., description="Desired state of the fan: True for ON, False for OFF")