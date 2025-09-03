from src.pii_redaction import detect_pii, redact_text

def test_redaction_masks_email_and_ssn():
    text = 'Contact me at jane.doe@example.com. SSN 123-45-6789.'
    findings = detect_pii(text)
    labels = {f['label'] for f in findings}
    assert 'EMAIL' in labels and 'SSN' in labels
    redacted = redact_text(text, findings)
    assert 'jane.doe@example.com' not in redacted
    assert '123-45-6789' not in redacted
