from uuid import uuid4
from src.utils.id_generator.constants import UNIQUE_TASK_ID_SUFFIX_LENGTH

class IdGenerator:
    def __init__(self, prefix:str):
        self.prefix = prefix
        self.unique_id = str(uuid4())[:UNIQUE_TASK_ID_SUFFIX_LENGTH]

    def generate_id(self) -> str:
        return f"{self.prefix}{self.unique_id}"
    @staticmethod
    def generate_id_from_unique_suffix(prefix: str, unique_suffix: str) -> str:
        return f"{prefix}{unique_suffix}"