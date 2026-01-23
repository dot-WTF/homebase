import sys
from langchain.messages import HumanMessage
from src.agent.agent import create_house_agent
from src.utils.audio import listen_for_audio, test_device_availabaility
from src.utils.stt import transcribe_audio
from enum import StrEnum

class InputCommands(StrEnum):
    INTERACT = "i"
    QUIT = "q"

def main():
    # Test audio device availability 
    is_audio_available = test_device_availabaility()
    assert is_audio_available, "No audio input device available."

    # Define agent with default configurations
    print("Creating house agent...")
    agent = create_house_agent()
    print("House agent created. Press 'Enter' to give a command or 'Esc' to exit.")

    while True:
        # MacOS is strict with detecting keyboard interactions so we use simple input prompts
        user_input = input("Enter command (i for interact, q for quit): ")
        if user_input == InputCommands.QUIT:
            print("Exiting program.")
            sys.exit(0)

        if user_input == InputCommands.INTERACT:
            try:  
                print("Listening for command...")
                user_command_audio = listen_for_audio() 
                print("Audio captured. Transcribing...")
                command_transcription = transcribe_audio(user_command_audio)
                print(f"Transcription: {command_transcription}")
                if command_transcription is not None:
                    print("Audio transcribed. Invoking agent...")
                    result = agent.invoke(
                        {"messages": [{"role": "user", "content": command_transcription}]}
                    )
                    print(f"Agent Response: {result}")
                else:
                    print("Failed to transcribe audio.")

            except Exception as e:
                # Gracefully handle errors during agent invocation
                print(f"Error during agent invocation: {e}")

if __name__ == "__main__":
    main()
