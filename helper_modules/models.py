import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


class RIReLU():
    
    def __init__(self, units=1000):
        '''
        A linear regressor that generates random ReLU features
        for every input dimension.


        Keyword arguments:
        
        units -- Integer that determines how many ReLU features are
                generated for each input feature (default 1000)
        '''
        self.model = LinearRegression()
        self.slopes = np.random.uniform(low=0, high=100, size=(1, units))
        self.intercepts = np.random.uniform(low=-10, high=10, size=(1, units))

    def fit(self, X, y):
        '''
        A function that fits the model
        

        Keyword arguments:
        X -- 2D array of shape (M, N), where M is the number of data points, and N the number of features
        y -- 1D array of shape (M,), where M is the number of data points
        '''
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
        '''
        A class that generates a polynomial model to describe the relation between
        a dependent and independent variable.

        Keyword arguments:
        degree -- integer that determines the degree of the polynomial model (default 2)
        '''
        self.poly = PolynomialFeatures(degree)
        self.linear = LinearRegression()
        self.pipe = Pipeline([('polynomial',self.poly),('modal',self.linear)])
    
    def fit(self, X, y):
        # self.linear.fit(self.poly(X), y)
        '''
        A function that fits the model.

        Keyword arguments:
        X -- 2D array of shape (M, N), where M is the number of data points, and N the number of features
        y -- 1D array of shape (M,), where M is the number of data points
        '''
        self.pipe.fit(X.reshape(-1,1),y)

    def predict(self, X):
        '''
        A function that predicts the model.

        Keyword arguments:
        X -- 2D array of shape (M, N), where M is the number of data points, and N the number of features
        '''
        return self.pipe.predict(X.reshape(-1,1))
    
    def score(self, X, y):
        '''
        A function that calculates the score (R^2 )of the model.

        Keyword arguments:
        X -- 2D array of shape (M, N), where M is the number of data points, and N the number of features
        y -- 1D array of shape (M,), where M is the number of data points
        '''
        y_true = y
        y_pred = self.predict(X)
        return r2_score(y_true, y_pred)

class Expofit(): #https://stackoverflow.com/questions/50706092/exponential-regression-function-python 
    def __init__(self):
        self.curve_fit = None # variable for holding the parameters we find (a, b, c)
        # i declare it here for transparency, so it's easier to find which variables we juggle around internally

    def func_exp(self, X):
        #c = 0
        return np.exp(self.curve_fit[0]) * np.exp(self.curve_fit[1]*X)
    
    def fit(self, X, y): # should rename to fit
        X = np.array(X).flatten() # flattens input array if not already flattened, since curve fit requires 1D arrays
        y = np.array(y).flatten() # same as above
        log_x_data = np.log(X)
        log_y_data = np.log(y)
        curve_fit = np.polyfit(X, log_y_data, 1)
        print("Found parameters! [a, b]: {}".format(str(curve_fit)))
       
        #popt, pcov = curve_fit(self.func_exp, X, y, p0 = (-1, 0.01, 1), maxfev=5000) # set number of guesses higher maxfev=5000
        #print("Found parameters! [a, b, c]: {}".format(str(popt)))
        
        print(type(curve_fit)) # useful function for seeing what type a variable is, (in this case, numpy array)
        self.curve_fit = curve_fit # saving found parameters

    def predict(self, X): # Same call pattern as in the plot above, notice the *, which unpacks our popt variable
        return self.func_exp(X) # not flattened here, so output will be like input in dimension
   
    def score(self, X, y): #IGNORE
        y_true = y
        y_pred = self.predict(X)
        return r2_score(y_true, y_pred)
    