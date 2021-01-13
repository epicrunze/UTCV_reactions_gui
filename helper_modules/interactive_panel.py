import tkinter as tk
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from . import datain, plot, models
from .models import RIReLU, Polyfit

class IntPanel(tk.Frame):
    def __init__(self, master=None, datadist=None):
        super().__init__(master)
        self.master = master
        self.datadist = datadist

        print(datadist)
        self.create_buttons()

    def create_buttons(self):
        self.create_linear_model = tk.Button(self)
        self.create_linear_model["text"] = "Create Linear Model"
        self.create_linear_model["command"] = self.create_model("linear")
        self.create_linear_model.pack(side="left")

        self.create_fancy_model = tk.Button(self)
        self.create_fancy_model["text"] = "Create Fancy Model"
        self.create_fancy_model["command"] = self.create_model("Polyfit")
        self.create_fancy_model.pack(side="left")

        self.get_pred_button = tk.Button(self)
        self.get_pred_button["text"] = "Clear"
        self.get_pred_button["command"] = plot.Plotter.clear_axis(datadist=self.datadist)
        self.get_pred_button.pack(side="left")
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.master.destroy)
        self.quit.pack(side="bottom")

    def create_model(self, modeltype):
        def temp_func():
            if not self.datadist.data:
                print("no data Sadge")
                return

            if modeltype == "linear":
                self.datadist.model = LinearRegression()
                self.fit_model()
                plot.Plotter.plot_model(legend="{:.3f}x + {:.3f}   R^2 = {:.3f}".format(self.datadist.model.coef_[0], self.datadist.model.intercept_, self.datadist.model_score), datadist=self.datadist)
            
            if modeltype == "RIReLU":
                self.datadist.model = RIReLU()
                self.fit_model()
                plot.Plotter.plot_model(legend="fancy model", datadist=self.datadist)
            
            if modeltype == "Polyfit":
                self.datadist.model = Polyfit()
                self.fit_model()
                plot.Plotter.plot_model(legend="polyfit", datadist=self.datadist)

        return temp_func

    def fit_model(self):
        if not self.datadist.data:
            print("no data Sadge")
            return
        if not self.datadist.model:
            print("no model Sadge")
            return
        
        if not self.datadist.get_vars():
            return

        self.datadist.model.fit(np.array(self.datadist.data[self.datadist.INDEPVAR]).reshape(-1, 1), self.datadist.data[self.datadist.DEPVAR])
        self.datadist.model_score = self.datadist.model.score(np.array(self.datadist.data[self.datadist.INDEPVAR]).reshape(-1, 1), self.datadist.data[self.datadist.DEPVAR])