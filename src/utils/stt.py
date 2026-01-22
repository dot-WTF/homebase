import io
from typing import Union
from openai import OpenAI
from src.config.env import OPENAI_API_KEY
from src.agent.models import OpenAIModels

openai_client = OpenAI(api_key=OPENAI_API_KEY)

def transcribe_audio(audio_file: io.BytesIO) -> Union[str, None]:
    try: 
        audio_file.seek(0)
        audio_file.name = "audio.wav"  # OpenAI API requires a filename attribute
        transcription = openai_client.audio.transcriptions.create(
            model = OpenAIModels.GPT_40_TRANSCRIBE,
            file = audio_file
        )
        return transcription.text
    except Exception as e:
        # Gracefully handle transcription errors
        print(f"Error during transcription: {e}")
        return None