from src.deduplication import cluster_near_duplicates

def test_dedup_clusters_similar_requests():
    texts = [
        'Budget documents for fiscal year 2022 regarding grants.',
        'Budget docs for FY22',
        'Emails mentioning cybersecurity threats in 2023.'
    ]
    clusters = cluster_near_duplicates(texts, threshold=0.3)
    lens = sorted([len(c) for c in clusters], reverse=True)
    assert lens[0] >= 2
