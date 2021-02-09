import numpy as np
import sklearn
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class Expofit(): #https://stackoverflow.com/questions/50706092/exponential-regression-function-python 
    def __init__(self):
        self.curve_fit = None # variable for holding the parameters we find (a, b, c)
        # i declare it here for transparency, so it's easier to find which variables we juggle around internally

    def func_exp(self, X):
        #c = 0
        # this code below harnesses numpy broadcasting, which I will explain once I compile a workshop notebook
        return np.exp(self.curve_fit[0]) * np.exp(self.curve_fit[1]*X)
    
    def exponential_regression(self, X, y): # should rename to fit
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
        return self.func_exp(X, *self.curve_fit) # not flattened here, so output will be like input in dimension
   
    def score(self, X, y): #IGNORE
        y_true = y
        y_pred = self.predict(X)
        return r2_score(y_true, y_pred)
    
if __name__ == "__main__":
    expofunc = Expofit()
    X = np.array([2, 3, 4, 4.5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14]).reshape(-1, 1)
    y = np.array([11.02, 16.19, 21.96, 19.5, 27.53, 32.75, 38.55, 42.94, 48.23, 54.38, 59.07, 63.11, 68.81, 80.81, 78.18, 75.27])

    expofunc.exponential_regression(X, y)
