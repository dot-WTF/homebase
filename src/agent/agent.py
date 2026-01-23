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
    model = ChatOpenAI(model=model_name, temperature=temperature, api_key=OPENAI_API_KEY)
    model = model.bind_tools(HOUSE_AGENT_TOOLS, tool_choice="required")
    model = model.with_retry(stop_after_attempt=3)
    agent = create_agent(
        model=model,
        tools=HOUSE_AGENT_TOOLS,
        system_prompt=SYSTEM_PROMPT,
    )
    return agent

