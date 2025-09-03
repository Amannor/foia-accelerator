import pandas as pd
from src.routing_classifier import RoutingClassifier

def test_routing_classifier_train_predict():
    df = pd.DataFrame({
        'text': [
            'All communications about immigration policy between 2021-2022.',
            'Budget documents for fiscal year 2022 regarding grants.',
            'Emails mentioning cybersecurity threats in 2023.',
            'Records related to water quality monitoring near refineries.'
        ],
        'label': ['DHS','OMB','CISA','EPA']
    })
    model = RoutingClassifier()
    model.fit(df['text'], df['label'])
    preds = model.predict(['Budget docs for FY22'])
    assert preds[0] in ['OMB']
