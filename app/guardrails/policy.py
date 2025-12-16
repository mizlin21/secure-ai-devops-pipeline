from app.guardrails.pii_detector import contains_pii
from app.guardrails.jailbreak_detector import is_jailbreak_attempt

SENSITIVE_TOPICS = [
    "build malware",
    "write ransomware",
    "steal passwords",
    "bypass firewall",
]

class GuardrailPolicy:
    """
    Central policy: decide allow/block with reasons.
    """

    def evaluate(self, message: str) -> dict:
        reasons: list[str] = []
        allowed = True

        if contains_pii(message):
            allowed = False
            reasons.append("Detected possible PII in user input.")

        if is_jailbreak_attempt(message):
            allowed = False
            reasons.append("Detected possible prompt-injection / jailbreak attempt.")

        for topic in SENSITIVE_TOPICS:
            if topic in message.lower():
                allowed = False
                reasons.append(f"Blocked sensitive topic: '{topic}'.")

        if allowed:
            reasons.append("All checks passed.")

        return {"allowed": allowed, "reasons": reasons}
