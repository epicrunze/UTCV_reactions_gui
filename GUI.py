#####################################################################################
# Program to intake a csv, read it, use a specified model, and make predictions     #
#####################################################################################

import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression

import tkinter as tk
import tkinter.filedialog

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from models import RIReLU, Polyfit

##############################
# MAIN PROGRAM

class MainProgram(tk.Frame):
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

    def create_outputs(self):
        self.prediction_frame = tk.LabelFrame(self, text="Predicted Value", padx=5, pady=5)
        self.prediction_frame.pack(side=tk.BOTTOM)

        self.prediction = tk.Label(self.prediction_frame)
        self.prediction.pack(side=tk.BOTTOM)

    def create_entries(self):

        self.vel_entry = tk.Entry()
        self.vel_entry.pack()
        
        # Create the velocity variable.
        self.vel_contents = tk.StringVar()
        # Set it to some value.
        self.vel_contents.set("Enter Velocity")
        # Tell the entry widget to watch this variable.
        self.vel_entry["textvariable"] = self.vel_contents

        self.dist_entry = tk.Entry()
        self.dist_entry.pack()

        # Create the distance variable.
        self.dist_contents = tk.StringVar()
        # Set it to some value.
        self.dist_contents.set("Enter Distance")
        # Tell the entry widget to watch this variable.
        self.dist_entry["textvariable"] = self.dist_contents

    def create_buttons(self):
        self.load_csv = tk.Button(self)
        self.load_csv["text"] = "Select csv to Load"
        self.load_csv["command"] = self.read_csv
        self.load_csv.pack(side="left")

        self.create_linear_model = tk.Button(self)
        self.create_linear_model["text"] = "Create Linear Model"
        self.create_linear_model["command"] = self.create_model("linear")
        self.create_linear_model.pack(side="left")

        self.create_linear_model = tk.Button(self)
        self.create_linear_model["text"] = "Create Fancy Model"
        self.create_linear_model["command"] = self.create_model("Polyfit")
        self.create_linear_model.pack(side="left")

        self.get_pred_button = tk.Button(self)
        self.get_pred_button["text"] = "Predict"
        self.get_pred_button["command"] = self.get_prediction
        self.get_pred_button.pack(side="left")

        self.get_pred_button = tk.Button(self)
        self.get_pred_button["text"] = "Clear"
        self.get_pred_button["command"] = self.clear_axis
        self.get_pred_button.pack(side="left")
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def create_plots(self):
        self.figure1 = plt.Figure(figsize=(6,5), dpi=100)
        self.ax = self.figure1.add_subplot(111)
        self.plot_canvas = FigureCanvasTkAgg(self.figure1, root)
        self.plot_canvas.get_tk_widget().pack(side=tk.TOP) 

    def plot_csv(self):
        if not self.get_vars():
            return

        self.ax.scatter(self.data[self.INDEPVAR], self.data[self.DEPVAR])

        self.ax.legend([self.DEPVAR]) 
        self.ax.set_xlabel(self.INDEPVAR)
        self.ax.set_title('{} Vs. {}'.format(self.DEPVAR, self.INDEPVAR))
        
        self.plot_canvas.draw()

    def read_csv(self):
        # csv or similar file with DEPVAR column, and TIME column
        filename = tk.filedialog.askopenfilename()
        
        # read csv as pandas df, then convert to dictionary
        self.data = pd.read_csv(filename).to_dict(orient="list")

        self.plot_csv()
    
    def create_model(self, modeltype):
        def temp_func():
            if not self.data:
                print("no data Sadge")
                return

            if modeltype == "linear":
                self.model = LinearRegression()
                self.fit_model()
                self.plot_model(legend="{:.3f}x + {:.3f}   R^2 = {:.3f}".format(self.model.coef_[0], self.model.intercept_, self.model_score))
            
            if modeltype == "RIReLU":
                self.model = RIReLU()
                self.fit_model()
                self.plot_model(legend="fancy model")
            
            if modeltype == "Polyfit":
                self.model = Polyfit()
                self.fit_model()
                self.plot_model(legend="polyfit")

        return temp_func

    def get_vars(self):
        if not self.data:
            print("no data Sadge")
            return None
        
        self.DEPVAR = [substr for substr in self.data.keys() if self.DEPVAR_indicator in substr]
        self.INDEPVAR = [substr for substr in self.data.keys() if self.INDEPVAR_indicator in substr]

        if len(self.DEPVAR) > 1:
            self.DEPVAR = None
            print("TOO MANY DEPENDENT VARS")
            return None
        
        if len(self.INDEPVAR) > 1:
            self.INDEPVAR = None
            print("TOO MANY INDEPENDENT VARS")
            return None
        
        self.DEPVAR = self.DEPVAR[0]
        self.INDEPVAR = self.INDEPVAR[0]

        return 1

    def fit_model(self):
        if not self.data:
            print("no data Sadge")
            return
        if not self.model:
            print("no model Sadge")
            return
        
        if not self.get_vars():
            return

        self.model.fit(np.array(self.data[self.INDEPVAR]).reshape(-1, 1), self.data[self.DEPVAR])
        self.model_score = self.model.score(np.array(self.data[self.INDEPVAR]).reshape(-1, 1), self.data[self.DEPVAR])
    
    def predict_model(self, X):

        return self.model.predict(np.array(X).reshape(-1, 1))

    def get_prediction(self):
        try:
            dist = float(self.dist_contents.get())
            velocity = float(self.vel_contents.get())
        except:
            print("non-valid entries")
            return

        # returns dep var
        time = dist / velocity

        pred = self.predict_model([time])

        print(pred)

        self.plot_prediction(time, pred[0])

        self.prediction["text"] = str(pred[0])

        return pred[0]
    
    def plot_prediction(self, x, y):

        self.ax.scatter([x], [y])
        
        self.plot_canvas.draw()

    def plot_model(self, legend="model"):
        if not self.get_vars():
            return
        
        lb = min(self.data[self.INDEPVAR])
        ub = max(self.data[self.INDEPVAR]) + 2

        self.ax.plot(np.linspace(lb, ub, num=100), self.predict_model(np.linspace(lb, ub, num=100)))

        self.ax.legend([legend]) 
        self.ax.set_xlabel(self.INDEPVAR)
        self.ax.set_title('{} Vs. {}'.format(self.DEPVAR, self.INDEPVAR))
        
        self.plot_canvas.draw()

    def clear_axis(self):
        if self.ax:
            self.ax.cla()
            self.plot_canvas.draw()

root = tk.Tk()
app = MainProgram(master=root)
app.mainloop()