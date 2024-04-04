import hashlib


def mask_string(string: str) -> str:
    """Reveals the first X chars of a string and masks the rest"""
    REVEALED_KEY_LEN = 10  # NOTE: strings shorter are completely exposed
    MASK = "**********"
    string_trimmed = string[:REVEALED_KEY_LEN]
    masked_string = string_trimmed + MASK
    return masked_string


def remove(
    collection: list[str] | list[list[str]], target: str
) -> list[str] | list[list[str]]:
    """Returns a copy of the collection w/o the target value"""
    new_collection = []
    for item in collection:
        if isinstance(item, str):
            if item != target:
                new_collection.append(item)
        elif isinstance(item, list):
            if target not in item:
                new_collection.append(item)
    return new_collection


def generate_key(value: str) -> str:
    """Generates a sha256 key"""
    KEY_PREFIX = "sk-"
    hash = hashlib.sha256(value.encode("utf-8"))
    hash_hex = hash.hexdigest()
    key = f"{KEY_PREFIX}{hash_hex}"
    return key
