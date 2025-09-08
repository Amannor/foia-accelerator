"""
Lightweight Extractive Summarizer (TextRank-like)
-------------------------------------------------
Implements a minimal extractive summarizer using a sentence similarity graph
with PageRank (via networkx). Avoids heavy model downloads.

Author: [Your Name]
License: MIT
"""
from typing import List
import re
import numpy as np
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SENT_SPLIT = re.compile(r'(?<=[.!?])\s+')

def split_sentences(text: str) -> List[str]:
    sents = [s.strip() for s in SENT_SPLIT.split(text) if s.strip()]
    return sents

def summarize(text: str, max_sentences: int = 3) -> str:
    sents = split_sentences(text)
    if len(sents) <= max_sentences:
        return text.strip()
    tfidf = TfidfVectorizer().fit_transform(sents)
    sim = cosine_similarity(tfidf)
    np.fill_diagonal(sim, 0.0)
    graph = nx.from_numpy_array(sim)
    scores = nx.pagerank(graph)
    ranked = sorted(((scores[i], s) for i, s in enumerate(sents)), reverse=True)
    top = [s for _, s in ranked[:max_sentences]]
    order = {s:i for i, s in enumerate(sents)}
    top_sorted = sorted(top, key=lambda s: order[s])
    return " ".join(top_sorted)
