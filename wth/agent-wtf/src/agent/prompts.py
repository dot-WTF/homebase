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

class HouseActionsPrompts(StrEnum):
    TOGGLE_LIGHT = TOGGLE_LIGHT
    SET_LIGHT = SET_LIGHT
