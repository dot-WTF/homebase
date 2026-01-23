import os 
import sys
import platform
import subprocess
from enum import StrEnum

# We use UNIX here to refer to any *NIX system including Linux and macOS
class MachineSystem(StrEnum):
    UNIX = "unix" 
    WINDOWS = "windows"

class PipExecutable(StrEnum):
    UNIX = "python3 -m pip" 
    WINDOWS = "python -m pip"    

class uvExecutable(StrEnum):
    UNIX = "python3 -m uv"
    WINDOWS = "python -m uv"

def setup_uv(system: MachineSystem) -> bool:
    pip_cmd = PipExecutable.UNIX if system == MachineSystem.UNIX else PipExecutable.WINDOWS
    try: 
        subprocess.run(f"{pip_cmd} install uv", shell=True, check=True)
    except Exception as e:
        print(f"ERROR INSTALLING UV:\n {e}")
        return False
    return True

def initialize_project()-> bool:
    try:
        subprocess.run(["uv", "init" "."], check=True) 
    except Exception as e:
        print(f"ERROR INITIALIZING PROJECT:\n {e}")
        return False
    return True

def setup_venv()-> bool:
    try:
        subprocess.run(["uv", "venv"], check=True) 
    except Exception as e:
        print(f"ERROR SETTING UP VENV:\n {e}")
        return False
    return True

def install_dependencies() -> bool: 
    try:
        subprocess.run(["uv", "sync"], check=True)
    except Exception as e:
        print(f"ERROR INSTALLING DEPENDENCIES:\n {e}")
        return False
    return True

def activate_venv(system: MachineSystem) -> bool:    
    activate_script = system == MachineSystem.WINDOWS and ".\\.venv\\Scripts\\activate" or "source .venv/bin/activate"
    try:
        subprocess.run(activate_script, shell=True, check=True)
    except Exception as e:
        print(f"ERROR ACTIVATING VENV:\n {e}")
        return False
    return True

def main():
    system = platform.system().lower() == MachineSystem.WINDOWS and MachineSystem.WINDOWS or MachineSystem.UNIX
    
    setup_uv_result = setup_uv(system)
    initialize_project_result = initialize_project()
    setup_venv_result = setup_venv()
    install_dependencies_result = install_dependencies()
    activate_venv_result = activate_venv(system)

    result_base = [
        setup_uv_result,
        initialize_project_result,
        setup_venv_result,
        install_dependencies_result,
        activate_venv_result
    ]

    if not all(result_base):
        print("One or more setup steps failed. Please check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main()