from enum import StrEnum

# Lights
TOGGLE_LIGHT = """
Use this tool whenever the user wants to toggle or switch a light without explicitly saying on or off.
This includes phrases like "toggle", "switch", or "flip the light".
Rooms: living, bedroom, kitchen, office, outdoor.
"""

SET_LIGHT = """
Use this tool whenever the user explicitly asks to turn a light on or off in a specific room.
This includes phrases like "turn on", "turn off", or "set the light".
Rooms: living, bedroom, kitchen, office, outdoor.
"""

# Doors
TOGGLE_DOOR = """
Use this tool whenever the user asks to toggle or switch the door state without clearly specifying open or close.
"""

SET_DOOR_OPEN = """
Use this tool whenever the user explicitly asks to open or close the door.
"""

# Thermostat
SET_THERMOSTAT = """
Use this tool whenever the user asks to change the thermostat temperature or mode.
Modes include heating, cooling, or off.
"""

# Alarm
TOGGLE_ALARM = """
Use this tool whenever the user asks to toggle or switch the alarm state without explicitly saying arm or disarm.
"""

SET_ALARM = """
Use this tool whenever the user explicitly asks to arm or disarm the alarm system.
"""

# Blinds
SET_BLINDS = """
Use this tool whenever the user asks to raise, lower, open, close, or set the position of blinds.
Percentage values may range from 0 to 100.
Rooms: living, bedroom.
"""

# Fans
TOGGLE_FAN = """
Use this tool whenever the user wants to toggle or switch a fan without specifying on or off.
Rooms: living, bedroom.
"""

SET_FAN = """
Use this tool whenever the user explicitly asks to turn a fan on or off in a room.
Rooms: living, bedroom.
"""

class HouseActionsPrompts(StrEnum):
    TOGGLE_LIGHT = TOGGLE_LIGHT
    SET_LIGHT = SET_LIGHT
    TOGGLE_DOOR = TOGGLE_DOOR
    SET_DOOR_OPEN = SET_DOOR_OPEN
    SET_THERMOSTAT = SET_THERMOSTAT
    TOGGLE_ALARM = TOGGLE_ALARM
    SET_ALARM = SET_ALARM
    SET_BLINDS = SET_BLINDS
    TOGGLE_FAN = TOGGLE_FAN
    SET_FAN = SET_FAN
