import numpy as np
import sklearn
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class Logfit(): #https://stackoverflow.com/questions/50706092/exponential-regression-function-python 
    def __init__(self):
        self.popt = None # variable for holding the parameters we find (a, b, c)
        # i declare it here for transparency, so it's easier to find which variables we juggle around internally

    def func_exp(self, X, a, b ,c):
        #c = 0
        # this code below harnesses numpy broadcasting, which I will explain once I compile a workshop notebook
        return a * np.exp(b * X) + c
    
    def exponential_regression(self, X, y): # should rename to fit
        X = np.array(X).flatten() # flattens input array if not already flattened, since curve fit requires 1D arrays
        y = np.array(y).flatten() # same as above
        popt, pcov = curve_fit(self.func_exp, X, y, p0 = (-1, 0.01, 1), maxfev=5000) # set number of guesses higher maxfev=5000
        print("Found parameters! [a, b, c]: {}".format(str(popt)))
        print(type(popt)) # useful function for seeing what type a variable is, (in this case, numpy array)
        self.popt = popt # saving found parameters

        #plotting code, to be removed
        puntos = plt.plot(X, y, 'x', color='xkcd:maroon', label = "data") 
        curve_regression = plt.plot(X, self.func_exp(X, *popt), color='xkcd:teal', label = "fit: {:.3f}, {:.3f}, {:.3f}".format(*popt))
        plt.legend()
        plt.show()
        return self.func_exp(X, *popt)

    def predict(self, X): # Same call pattern as in the plot above, notice the *, which unpacks our popt variable
        return self.func_exp(X, *self.popt) # not flattened here, so output will be like input in dimension
   
    def score(self, X, y): #IGNORE
        #TODO Implement R^2?, or if there's a better metric, implement that, but R^2 is consistent with our other models
        pass
    
if __name__ == "__main__":
    logfunc = Logfit()
    X = np.array([2, 3, 4, 4.5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14]).reshape(-1, 1)
    y = np.array([11.02, 16.19, 21.96, 19.5, 27.53, 32.75, 38.55, 42.94, 48.23, 54.38, 59.07, 63.11, 68.81, 80.81, 78.18, 75.27])

    logfunc.exponential_regression(X, y)
