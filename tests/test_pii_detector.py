from app.guardrails.pii_detector import contains_pii

def test_detects_email():
    assert contains_pii("Contact me at linda@example.com") is True

def test_detects_phone():
    assert contains_pii("My phone is (555) 123-4567") is True

def test_detects_ssn():
    assert contains_pii("SSN: 123-45-6789") is True

def test_no_pii():
    assert contains_pii("I like cybersecurity and coffee.") is False
