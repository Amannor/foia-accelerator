"""
Deduplication via TF-IDF + Cosine Similarity
--------------------------------------------
Clusters near-duplicate FOIA requests using cosine similarity on TF-IDF vectors.
No heavy models required. Threshold controls cluster tightness.

Author: Alon Mannor
License: MIT
"""
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def cluster_near_duplicates(texts: List[str], threshold: float = 0.75) -> List[List[int]]:
    if not texts:
        return []
    tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1,2)).fit_transform(texts)
    sim = cosine_similarity(tfidf)
    parent = list(range(len(texts)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a,b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    n = len(texts)
    for i in range(n):
        for j in range(i+1, n):
            if sim[i, j] >= threshold:
                union(i, j)

    groups: Dict[int, List[int]] = {}
    for i in range(n):
        r = find(i)
        groups.setdefault(r, []).append(i)
    return list(groups.values())
