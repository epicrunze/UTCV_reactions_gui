import tkinter as tk
import pandas as pd
from . import plot


# code for data intake widget
class DataIntake(tk.Frame):
    def __init__(self, master=None, datadist=None):
        '''function that defines the data intake panel
            right now only the read csv button

            inputs:
                master: tkinter frame object that this frame
                        should be attached to
                datadist: DataDistributor object
        '''
        super().__init__(master)  # initializing the master tkinter frame
        self.master = master
        self.datadist = datadist

        self.create_buttons()

    def create_buttons(self):
        '''creates the button for loading csv'''
        self.load_csv = tk.Button(self)
        self.load_csv["text"] = "Select csv to Load"
        self.load_csv["command"] = self.read_csv(datadist=self.datadist)
        self.load_csv.pack()

    @classmethod
    def read_csv(cls, datadist=None):
        '''returns a csv reading function, utilizing the file dialog'''
        def tmp():
            # csv or similar file with DEPVAR column, and TIME column
            filename = tk.filedialog.askopenfilename()

            # read csv as pandas df, then convert to dictionary
            datadist.data = pd.read_csv(filename).to_dict(orient="list")

            plot.Plotter.plot_csv(datadist=datadist)

        return tmp
