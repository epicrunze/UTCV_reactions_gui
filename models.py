import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

class RIReLU():
    # model that does fun stuff
    def __init__(self, units=1000):
        self.model = LinearRegression()
        self.slopes = np.random.uniform(low=0, high=100, size=(1, units))
        self.intercepts = np.random.uniform(low=-10, high=10, size=(1, units))

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

class Polyfit():
    # https://www.analyticsvidhya.com/blog/2020/03/polynomial-regression-python/
    def __init__(self, degree = 2):
        self.poly = PolynomialFeatures(degree)
        self.linear = LinearRegression()
        self.pipe = Pipeline([('polynomial',self.poly),('modal',self.linear)])
    
    def fit(self, X, y):
        # self.linear.fit(self.poly(X), y)
        self.pipe.fit(X.reshape(-1,1),y)

    def predict(self, X):
        return self.pipe.predict(X.reshape(-1,1))
    
    def score(self, X, y):
        y_true = y
        y_pred = self.predict(X)
        return r2_score(y_true, y_pred)