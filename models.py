import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

class RIReLU():
    # model that does fun stuff
    def __init__(self, units=1000):
        self.model = LinearRegression()
        self.slopes = np.random.uniform(low=0, high=100, size=(1, 1000))
        self.intercepts = np.random.uniform(low=-10, high=10, size=(1, 1000))

    def fit(self, X, y):
        stick = X * self.slopes + self.intercepts
        X = np.max(np.stack((stick, np.zeros_like(stick))), axis=0)
        self.model.fit(X, y)
    
    def predict(self, X):
        stick = X * self.slopes + self.intercepts
        X = np.max(np.stack((stick, np.zeros_like(stick))), axis=0)

        return self.model.predict(X)
    
    def score(self, X, y):
        stick = X * self.slopes + self.intercepts
        X = np.max(np.stack((stick, np.zeros_like(stick))), axis=0)

        return self.model.score(X, y)

class polyfit():
    # https://www.analyticsvidhya.com/blog/2020/03/polynomial-regression-python/
    def __init__(self, degree = 2, units = 1000):
        self.poly = PolynomialFeatures(degree)
        self.linear = LinearRegression()
        self.pipe = Pipeline([('polynomial',self.poly),('modal',self.linear)])
    
    def fit(self, X, y):
        self.pipe.fit(X.reshape(-1,1),y.reshape(-1,1))

    def predict(self, X):
        return self.pipe.predict(X.reshape(-1,1))