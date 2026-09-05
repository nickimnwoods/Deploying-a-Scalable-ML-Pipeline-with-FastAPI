from ml.model import compute_model_metrics
from ml.model import train_model
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split


def test_compute_model_metrics():
    """
    Test compute_model_metrics by entering values that should result
    precision, recall and fbeta all equaling 1
    """
    y = [1, 0, 1, 0]
    preds = [1, 0, 1, 0]

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert precision == 1.0
    assert recall == 1.0
    assert fbeta == 1.0


def test_verify_model():
    """
    Verify train_model returns the expected algorithm of RandomForest
    """
    X_train = [[1], [2], [3], [4], [5]]
    y_train = [1, 0, 1, 1, 0]

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


def test_train_test_split():
    """
    test that train_test_split produces datasets of the expected size
    """
    # create dummy data frame to use for test
    data = pd.DataFrame({
        "age": [25, 32, 47, 51, 29, 38, 44, 60, 22, 35],
        "education": [
            "Bachelors", "HS-grad", "Masters", "HS-grad",
            "Bachelors", "Some-college", "Doctorate",
            "HS-grad", "Bachelors", "Masters"
            ],
        "salary": [
            "<=50K", "<=50K", ">50K", "<=50K", "<=50K",
            "<=50K", ">50K", "<=50K", "<=50K", ">50K"
            ]
    })

    train, test = train_test_split(data, test_size=0.20, random_state=55)

    assert len(train) + len(test) == len(data)
