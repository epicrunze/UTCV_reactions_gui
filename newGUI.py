import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression

import tkinter as tk
import tkinter.filedialog

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from helper_modules.data import DataDistributor
from helper_modules.datain import DataIntake
from helper_modules.plot import Plotter
from helper_modules.interactive_panel import IntPanel
from helper_modules.prediction import PredPanel

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # creating a data distributor to distribute data
        self.datadist = DataDistributor()

        # creating tkinter widgets 

        # creating data intake frame
        self.dataintake = DataIntake(master=self, datadist=self.datadist)
        self.dataintake.grid(column=20, row=0, columnspan=20, rowspan=20)

        self.intpanel = IntPanel(master=self, datadist=self.datadist)
        self.intpanel.grid(column=0, row=0, columnspan=20, rowspan=20)

        self.plotter = Plotter(master=self, datadist=self.datadist)
        self.plotter.grid(column=0, row=20, columnspan=20, rowspan=20)

        self.predpanel = PredPanel(master=self, datadist=self.datadist)
        self.predpanel.grid(column=20, row=20, columnspan=20, rowspan=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(master=root)
    app.mainloop()

