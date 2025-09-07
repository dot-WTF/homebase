class IdGenerator:
    @staticmethod
    def generate_id(prefix: str, unique_suffix: str) -> str:
        return f"{prefix}{unique_suffix}"