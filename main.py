import sys
from src.agent.agent import create_house_agent
from src.utils.audio import listen_for_audio, test_device_availabaility
from src.utils.stt import transcribe_audio
from src.utils.ux import it_prints_if_not_none, extract_ai_message, extract_tool_message, printify, MessageTypes
from src.utils.exception import suppress_stderr
from enum import StrEnum

class InputCommands(StrEnum):
    SPEAK = "s"
    QUIT = "q"

def main():
    # Test audio device availability 
    is_audio_available = test_device_availabaility()
    assert is_audio_available, "No audio input device available."

    # Define agent with default configurations
    printify("Creating house agent...", MessageTypes.SYSTEM_MESSAGE)
    agent = create_house_agent()

    while True:
        # MacOS is strict with detecting keyboard interactions so we use simple input prompts
        user_input = input("Enter command (s to speak, q for quit, or any instruction for the agent): ")
        if user_input == InputCommands.QUIT:
            printify("Exiting program.", MessageTypes.SYSTEM_MESSAGE)
            sys.exit(0)

        if user_input == InputCommands.SPEAK:
            try:  
                printify("Listening for command...", MessageTypes.SYSTEM_MESSAGE)
                with suppress_stderr():
                    user_command_audio = listen_for_audio() 
                printify("Audio captured. Transcribing...", MessageTypes.SYSTEM_MESSAGE)
                command_transcription = transcribe_audio(user_command_audio)
                printify(f"Transcription: {command_transcription}", MessageTypes.SYSTEM_MESSAGE)
                if command_transcription is not None:
                    printify("Audio transcribed. Invoking agent...", MessageTypes.SYSTEM_MESSAGE)
                    result = agent.invoke(
                        {"messages": [{"role": "user", "content": command_transcription}]}
                    )

                    ai_message = extract_ai_message(result["messages"])
                    tool_message = extract_tool_message(result["messages"])

                    printify(ai_message, MessageTypes.AI_MESSAGE)
                    printify(tool_message, MessageTypes.TOOL_MESSAGE)

                else:
                    printify("Failed to transcribe audio.", MessageTypes.SYSTEM_MESSAGE)
            except Exception as e:
                # Gracefully handle errors during audio capture or transcription
                printify(f"Error during audio processing: {e}", MessageTypes.SYSTEM_MESSAGE)
            finally:
                continue  # Go back to the start of the loop after handling audio input
            
        user_commnad = user_input.strip()
        if user_commnad:
            try:
                printify("Invoking agent...", MessageTypes.SYSTEM_MESSAGE)

                result = agent.invoke(
                    {"messages": [{"role": "user", "content": user_commnad}]}
                )
                ai_message = extract_ai_message(result["messages"])
                tool_message = extract_tool_message(result["messages"])

                printify(ai_message, MessageTypes.AI_MESSAGE)
                printify(tool_message, MessageTypes.TOOL_MESSAGE)
            except Exception as e:
                # Gracefully handle errors during agent invocation
                printify(f"Error during agent invocation: {e}", MessageTypes.SYSTEM_MESSAGE)
            finally:
                continue # Go back to the start of the loop after handling text input

if __name__ == "__main__":
    main()
