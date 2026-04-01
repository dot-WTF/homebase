import os 
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")    
assert OPENAI_API_KEY is not None, "OPENAI_API_KEY environment variable is not set."

HOUSE_ID = os.getenv("HOUSE_ID")
assert HOUSE_ID is not None, "Your HOUSE_ID environment variable is not set."

RESOURCE_URL = os.getenv("RESOURCE_URL")
assert RESOURCE_URL is not None, "Your RESOURCE_URL environment variable is not set."