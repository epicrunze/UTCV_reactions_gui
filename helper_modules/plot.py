import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np

class Plotter(tk.Frame):
    def __init__(self, master=None, datadist=None):
        super().__init__(master)
        self.master = master
        self.datadist = datadist

        self.create_plots()

    def create_plots(self):

        self.datadist.figure1 = plt.Figure(figsize=(6,5), dpi=100)
        self.datadist.ax = self.datadist.figure1.add_subplot(111)
        self.datadist.plot_canvas = FigureCanvasTkAgg(self.datadist.figure1, self)
        self.datadist.plot_canvas.get_tk_widget().pack(side=tk.BOTTOM)

    @classmethod
    def plot_csv(cls, datadist=None):
        if not datadist.get_vars():
            return

        datadist.ax.scatter(datadist.data[datadist.INDEPVAR], datadist.data[datadist.DEPVAR])

        datadist.ax.legend([datadist.DEPVAR]) 
        datadist.ax.set_xlabel(datadist.INDEPVAR)
        datadist.ax.set_title('{} Vs. {}'.format(datadist.DEPVAR, datadist.INDEPVAR))
        
        datadist.plot_canvas.draw()

    @classmethod
    def plot_model(cls, datadist=None, legend="model"):
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
        def tmp():
            if datadist.ax:
                datadist.ax.cla()
                datadist.plot_canvas.draw()
        return tmp
