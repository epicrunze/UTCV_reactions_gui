import tkinter as tk
import pandas as pd
from . import plot

# code for data intake widget
class DataIntake(tk.Frame):
    def __init__(self, master=None, datadist=None):
        super().__init__(master)
        self.master = master
        self.datadist = datadist

        self.create_buttons()

        # parameters governing csv intake

    def create_buttons(self):
        self.load_csv = tk.Button(self)
        self.load_csv["text"] = "Select csv to Load"
        self.load_csv["command"] = self.read_csv(datadist=self.datadist)
        self.load_csv.pack()

    @classmethod
    def read_csv(cls, datadist=None):
        def tmp():
            # csv or similar file with DEPVAR column, and TIME column
            filename = tk.filedialog.askopenfilename()
            
            # read csv as pandas df, then convert to dictionary
            datadist.data = pd.read_csv(filename).to_dict(orient="list")

            plot.Plotter.plot_csv(datadist=datadist)
        
        return tmp

    