# Build: 2eed65b9d9a162880b6998d8be82d31b

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
