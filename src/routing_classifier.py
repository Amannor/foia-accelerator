from __future__ import annotations
"""
Routing Classifier
------------------
A lightweight text classifier (TF-IDF + Logistic Regression) that suggests a target
component/agency for an incoming FOIA request.

- Deterministic, small, easy to train on a laptop/GPU-less machine.
- Optional: swap to a transformer-based classifier (see comments).

Author: Alon Mannor
License: MIT
"""
from typing import List, Iterable
from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
import numpy as np

@dataclass
class RoutingModelArtifacts:
    pipeline: Pipeline
    label_encoder: LabelEncoder

class RoutingClassifier:
    def __init__(self, max_features: int = 5000, C: float = 2.0, random_state: int = 42):
        self.vectorizer = TfidfVectorizer(max_features=max_features, ngram_range=(1,2))
        self.clf = LogisticRegression(max_iter=1000, C=C, n_jobs=None, random_state=random_state)
        self.pipe = Pipeline([('tfidf', self.vectorizer), ('clf', self.clf)])
        self.le = LabelEncoder()
        self.is_fit = False

    def fit(self, texts: Iterable[str], labels: Iterable[str]) -> RoutingModelArtifacts:
        y = self.le.fit_transform(list(labels))
        self.pipe.fit(list(texts), y)
        self.is_fit = True
        return RoutingModelArtifacts(self.pipe, self.le)

    def predict(self, texts: Iterable[str]) -> List[str]:
        assert self.is_fit, "Model not fit. Call fit() first."
        yhat = self.pipe.predict(list(texts))
        return self.le.inverse_transform(yhat).tolist()

    def predict_proba(self, texts: Iterable[str]) -> np.ndarray:
        assert self.is_fit, "Model not fit. Call fit() first."
        return self.pipe.predict_proba(list(texts))

# Optional transformer starter (commented):
# from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
# Use when you want a neural model; keep classical baseline as default for reliability.
