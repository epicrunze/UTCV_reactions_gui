#test file used while creating the polyfit class in models.py
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import pandas as pd

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
X=10*np.random.normal(0,1,70)
y=10*(-X**2)+np.random.normal(-100,100,70)

model = polyfit(degree=2)
model.fit(X,y)
poly_pred = model.predict(X)
sorted_zip = sorted(zip(X,poly_pred))
x_poly, poly_pred = zip(*sorted_zip)
plt.figure(figsize=(10,6))
plt.scatter(X,y,s=15)
plt.plot(x_poly,poly_pred,color='g',label='Polynomial Regression')
plt.xlabel('Predictor',fontsize=16)
plt.ylabel('Target',fontsize=16)
plt.legend()
plt.show()