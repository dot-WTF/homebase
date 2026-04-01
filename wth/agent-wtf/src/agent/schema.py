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
    TOGGLE_DOOR_LOCK = "toggleLock"
    SET_DOOR_LOCK = "setLock"
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
    on: bool = Field(..., description="Desired state of the light: True for ON, False for OFF")
