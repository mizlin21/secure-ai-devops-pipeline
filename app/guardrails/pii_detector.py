import re

EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
PHONE_REGEX = re.compile(r"\b(\+?\d{1,2}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b")
SSN_REGEX = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")

def contains_pii(text: str) -> bool:
    """
    Simple PII detection (demo-grade but explainable):
    - email
    - phone
    - SSN
    """
    if EMAIL_REGEX.search(text):
        return True
    if PHONE_REGEX.search(text):
        return True
    if SSN_REGEX.search(text):
        return True
    return False
