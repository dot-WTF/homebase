import sounddevice as sd 
import io 
import soundfile as sf
from typing import Union

DURATION = 5  # seconds
FS = 44100  # Sample rate

def test_device_availabaility() -> bool:
    try:
        sd.check_input_settings()
        return True
    except Exception as e:
        print(f"Audio device check failed: {e}")
        return False
    
def listen_for_audio(duration: int = DURATION, fs: int = FS) -> Union[bytes, None]:
    try: 
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()  

        buffer = io.BytesIO()
        sf.write(buffer, recording, fs, format="WAV")
        buffer.seek(0)
        return buffer.read()
    except Exception as e:
        print(f"Error during audio recording: {e}")
        return None