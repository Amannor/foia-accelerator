from src.summarizer import summarize

def test_summarizer_returns_shorter_text():
    text = (
        'The agency received a significant number of requests this year. '
        'Processing times increased due to staffing shortages. '
        'However, new tooling improved triage. '
        'Future investments could reduce the backlog.'
    )
    out = summarize(text, max_sentences=2)
    assert len(out) < len(text)
    assert out.count('.') <= 3
