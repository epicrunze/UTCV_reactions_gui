import numpy as np
import sklearn
#lol Olevia's attempt to code - exponential regression - i essentially linearized stick
from sklearn.linear_model import LinearRegression

class RIReLU():
    # model that does fun stuff
    def __init__(self, units=1000):
        self.model = LinearRegression()
        self.slopes = np.random.uniform(low=0, high=100, size=(1, 1000))
        self.intercepts = np.random.uniform(low=-10, high=10, size=(1, 1000))

    def fit(self, X, y):#how do u get rid of the error underline thing?
        stick = np.exp(X*self.slopes + np.log(self.intercepts))
        X = np.max(np.stack((stick, np.zeros_like(stick))), axis=0)
        self.model.fit(X, y)
    
    def predict(self, X):
        stick = np.exp(X * self.slopes + np.log(self.intercepts))
        X = np.max(np.stack((stick, np.zeros_like(stick))), axis=0)
        return self.model.predict(X)
    
    def score(self, X, y):
        stick = np.exp(X* self.slopes + np.log(self.intercepts))
        X = np.max(np.stack((stick, np.zeros_like(stick))), axis=0)

        return self.model.score(X, y)