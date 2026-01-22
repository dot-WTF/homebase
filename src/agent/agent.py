import os 
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from src.agent.models import OpenAIModels
from src.agent.tools import HOUSE_AGENT_TOOLS

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")    
assert OPENAI_API_KEY is not None, "OPENAI_API_KEY environment variable is not set."


def create_model(model_name: str, temperature: float = 0) -> ChatOpenAI:
    return ChatOpenAI(
        model_name=model_name,
        temperature=temperature,
        openai_api_key=OPENAI_API_KEY  
    )

def create_house_agent(model_name: str, temperature: float = 0, verbose: bool = True) -> any:
    llm = create_model(model_name, temperature=temperature)
    agent = create_agent(
        llm=llm,
        tools=HOUSE_AGENT_TOOLS,
        verbose=verbose
    )
    return agent

