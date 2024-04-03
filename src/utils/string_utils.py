def mask_string(string: str) -> str:
    """
    Reveals the first X chars of a string and masks the rest
    """
    REVEALED_KEY_LEN = 10  # NOTE: strings shorter are completely exposed
    MASK = "**********"
    string_trimmed = string[:REVEALED_KEY_LEN]
    masked_string = string_trimmed + MASK
    return masked_string
