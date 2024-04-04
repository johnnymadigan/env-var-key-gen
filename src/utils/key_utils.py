from src.constants.consts import KEY_PREFIX
import hashlib


def generate_key(value: str) -> str:
    """Generates a sha256 key"""
    hash = hashlib.sha256(value.encode("utf-8"))
    hash_hex = hash.hexdigest()
    key = f"{KEY_PREFIX}{hash_hex}"
    return key
