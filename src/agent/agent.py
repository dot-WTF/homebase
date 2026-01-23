from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from src.agent.models import OpenAIModels
from src.agent.tools import HOUSE_AGENT_TOOLS
from src.config.env import OPENAI_API_KEY

SYSTEM_PROMPT = '''
You are a smart home assistant. When users request home control actions, you MUST use the available tools with EXACT parameter values.

CRITICAL: Always use these EXACT action values:
- Lights: action="toggleLight" OR action="setLight"
- Doors: action="toggleDoor" OR action="setDoorOpen" OR action="toggleDoorLock" OR action="setDoorLock"  
- Thermostat: action="setThermostat"
- Fans: action="toggleFan" OR action="setFan"
- Blinds: action="setBlinds"
- Alarm: action="toggleAlarm" OR action="setAlarm"

Available rooms: living, kitchen, office, bedroom, outdoor (for lights), living/bedroom (for fans/blinds)

Always use tools for control requests.
'''

def create_house_agent(model_name: str = OpenAIModels.GPT_4O_MINI, temperature: float = 0) -> any:
    pass

