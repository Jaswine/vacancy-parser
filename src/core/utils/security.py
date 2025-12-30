import secrets
import hashlib

def generate_code(length: int = 6) -> str:
    return ''.join(secrets.choice("0123456789") for _ in range(length))

def hash_code(code: str) -> str:
    return hashlib.sha256(code.encode()).hexdigest()