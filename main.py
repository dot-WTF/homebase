import keyboard
from src.agent.agent import create_house_agent
from src.utils.audio import listen_for_audio, test_device_availabaility
from src.utils.stt import transcribe_audio

def main():
    # Test audio device availability 
    is_audio_available = test_device_availabaility()
    assert is_audio_available, "No audio input device available."

    # Define agent with default configurations
    print("Creating house agent...")
    agent = create_house_agent()
    print("House agent created. Press 'Enter' to give a command or 'Esc' to exit.")

    while True:
        if keyboard.is_pressed('esc'):
            print("Exiting program.")
            break

        if keyboard.is_pressed('enter'):
            try:  
                user_command_audio = listen_for_audio() 
                command_transcription = transcribe_audio(user_command_audio)
                if command_transcription is not None:
                    result = agent.invoke(command_transcription)
                    print(f"Agent Response: {result}")
                else:
                    print("Failed to transcribe audio.")

            except Exception as e:
                # Gracefully handle errors during agent invocation
                print(f"Error during agent invocation: {e}")

if __name__ == "__main__":
    main()
