JAILBREAK_PATTERNS = [
    "ignore previous instructions",
    "ignore all previous instructions",
    "you are now in developer mode",
    "bypass safety",
    "act as an unfiltered model",
    "do anything now",
    "dan mode",
]

def is_jailbreak_attempt(text: str) -> bool:
    """
    Heuristic detection of common jailbreak phrases.
    """
    lower = text.lower()
    return any(pattern in lower for pattern in JAILBREAK_PATTERNS)
