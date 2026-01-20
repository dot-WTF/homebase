from enum import StrEnum

# Light prompts
toggle_light_prompt = '''
'''

set_light_prompt = '''
'''

# Door prompts
toggle_door_prompt = '''
'''

toggle_door_lock_prompt = '''
'''

set_door_open_prompt = '''
'''

set_door_lock_prompt = '''
'''
# Thermostat prompts
set_thermostat_prompt = '''
'''

toggle_alarm_prompt = '''
'''

# Alarm prompts
set_alarm_prompt = '''
'''

# Blinds prompts
set_blinds_prompt = '''
'''

# Fan prompts
toggle_fan_prompt = '''
'''

set_fan_prompt = '''
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
