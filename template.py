from sktime.base import BaseEstimator

class YourAlgorithm(BaseEstimator):
    def __init__(self, your_params):
pass

    def fit(self, X, y):
pass

    def predict(self, X):
pass
from sktime.transformers.base import BaseTransformer
from sktime.classifiers.base import BaseClassifier

class YourAlgorithm(BaseTransformer):
from sktime.registry import register_estimator

@register_estimator()
class YourAlgorithm(BaseEstimator):
