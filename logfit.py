import numpy as np
import sklearn
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class Logfit(): #https://stackoverflow.com/questions/50706092/exponential-regression-function-python 
    def __init__(self, a, b, c):
        self.a = a 
        self.b = b 
        self.c = c 

    def func_exp(self, X):
        #c = 0
        return a * np.exp(b * X) + c
    
    def exponential_regression (X, y):
        popt, pcov = curve_fit(func_exp, X, y, p0 = (-1, 0.01, 1))
         print(popt)
         puntos = plt.plot(X, y, 'x', color='xkcd:maroon', label = "data")
         curve_regression = plt.plot(x, func_exp(X, *popt), color='xkcd:teal', label = "fit: {:.3f}, {:.3f}, {:.3f}".format(*popt))
         plt.legend()
         plt.show()
         return func_exp(X, *popt)

    def predict(self, X): #IGNORE HAVE NOT FINISHED
        return self.predict(X.reshape(-1,1))
   
    def score(self, X, y): #IGNORE
        return self.model.score(X, y)