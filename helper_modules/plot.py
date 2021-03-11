import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np


class Plotter(tk.Frame):
    def __init__(self, master=None, datadist=None):
        '''
        Class for a plot widget. Used as a subframe for the main frame
        Generates a matplotlib figure and axes, placed in the datadist object

        inputs:
            master: master frame that holds this widget
            datadist: a DataDistributor object
        '''

        super().__init__(master)
        self.master = master
        self.datadist = datadist

        self.create_plots()

    def create_plots(self):
        '''
        Function to create a matplotlib plot to operate on
        changes DataDistributor object in place
        '''

        self.datadist.figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        self.datadist.ax = self.datadist.figure1.add_subplot(111)
        self.datadist.plot_canvas = FigureCanvasTkAgg(self.datadist.figure1, self)
        self.datadist.plot_canvas.get_tk_widget().pack(side=tk.BOTTOM)

    @classmethod
    def plot_csv(cls, datadist=None):
        '''
        Function to plot a csv, from data already placed in the
        DataDistributor object

        inputs:
            datadist: DataDistributor object that has
                a csv loaded in
        
        outputs:
            None

        In place operation that affects the datadist axes
        '''
        if not datadist.get_vars():
            return

        datadist.ax.scatter(datadist.data[datadist.INDEPVAR], datadist.data[datadist.DEPVAR])

        datadist.ax.legend([datadist.DEPVAR]) 
        datadist.ax.set_xlabel(datadist.INDEPVAR)
        datadist.ax.set_title('{} Vs. {}'.format(datadist.DEPVAR, datadist.INDEPVAR))
        
        datadist.plot_canvas.draw()

    @classmethod
    def plot_model(cls, datadist=None, legend="model"):
        '''
        Function that plots a model based on data in the datadist

        inputs:
            datadist: DataDistributor object
            legend: string to use as the plotted legend
        
        outputs:
            None
        
        operates on datadist axis in place

        Quite hard coded, with arbitrary value 2 placed to expand the 
        bounds plotted
        Only 100 data points for line interpolation
        '''
        if not datadist.get_vars():
            return
        
        lb = min(datadist.data[datadist.INDEPVAR])
        ub = max(datadist.data[datadist.INDEPVAR]) + 2

        datadist.ax.plot(np.linspace(lb, ub, num=100), datadist.model.predict(np.linspace(lb, ub, num=100).reshape(-1, 1)))

        datadist.ax.legend([legend]) 
        datadist.ax.set_xlabel(datadist.INDEPVAR)
        datadist.ax.set_title('{} Vs. {}'.format(datadist.DEPVAR, datadist.INDEPVAR))
        
        datadist.plot_canvas.draw()
    
    @classmethod
    def clear_axis(cls, datadist=None):
        '''helper function to clear axis in a datadist'''
        def tmp():
            if datadist.ax:
                datadist.ax.cla()
                datadist.plot_canvas.draw()
        return tmp
