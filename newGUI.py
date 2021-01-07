import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression

import tkinter as tk
import tkinter.filedialog

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from models import RIReLU


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Data is a dictionary of lists, with column headers as keys
        self.data = None
        self.model = None
        self.ax = None
        self.plot_canvas = None

        self.create_buttons()
        self.create_entries()
        self.create_plots()
        self.create_outputs()
    
        # csv PARAMETERS
        self.DEPVAR_indicator = "DEPVAR"
        self.INDEPVAR_indicator = "TIME"

        self.DEPVAR = None
        self.INDEPVAR = None