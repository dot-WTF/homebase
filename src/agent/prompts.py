from enum import StrEnum

# Light prompts
toggle_light_prompt = '''
Toggle a light in a specific room.
Rooms: living, bedroom, kitchen, office, outdoor
Example: {"action": "toggleLight", "params": {"room": "living"}}
'''

set_light_prompt = '''
Set light to specific state in a room.
Rooms: living, bedroom, kitchen, office, outdoor
Example: {"action": "setLight", "params": {"room": "bedroom", "isOn": true}}
'''

# Door prompts
toggle_door_prompt = '''
Toggle door open/close state.
Example: {"action": "toggleDoor"}
'''

toggle_door_lock_prompt = '''
Toggle door lock state.
Example: {"action": "toggleLock"}
'''

set_door_open_prompt = '''
Set door open/close state.
Example: {"action": "setDoorOpen", "params": {"isOpen": true}}
'''

set_door_lock_prompt = '''
Set door lock state.
Example: {"action": "setLock", "params": {"isLocked": true}}
'''
# Thermostat prompts
set_thermostat_prompt = '''
Set thermostat temperature and mode.
Modes: heating, cooling, off
Example: {"action": "setThermostat", "params": {"target": 24, "mode": "heating"}}
'''

toggle_alarm_prompt = '''
Toggle alarm state.
Example: {"action": "toggleAlarm"}
'''

# Alarm prompts
set_alarm_prompt = '''
Set alarm armed/disarmed state.
Example: {"action": "setAlarm", "params": {"isArmed": true}}
'''

# Blinds prompts
set_blinds_prompt = '''
Set blind position (0-100 percentage).
Rooms: living, bedroom
Example: {"action": "setBlinds", "params": {"room": "living", "percentage": 75}}
'''

# Fan prompts
toggle_fan_prompt = '''
Toggle fan in a specific room.
Rooms: living, bedroom
Example: {"action": "toggleFan", "params": {"room": "living"}}
'''

set_fan_prompt = '''
Set fan state in a specific room.
Rooms: living, bedroom
Example: {"action": "setFan", "params": {"room": "bedroom", "isOn": true}}
'''

class HouseActionsPrompts(StrEnum):
    TOGGLE_LIGHT = toggle_light_prompt  
    SET_LIGHT = set_light_prompt
    TOGGLE_DOOR = toggle_door_prompt
    TOGGLE_DOOR_LOCK = toggle_door_lock_prompt
    SET_DOOR_OPEN = set_door_open_prompt
    SET_DOOR_LOCK = set_door_lock_prompt
    SET_THERMOSTAT = set_thermostat_prompt
    TOGGLE_ALARM = toggle_alarm_prompt
    SET_ALARM = set_alarm_prompt
    SET_BLINDS = set_blinds_prompt
    TOGGLE_FAN = toggle_fan_prompt
    SET_FAN = set_fan_prompt
