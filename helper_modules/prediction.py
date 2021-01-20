import tkinter as tk
import numpy as np

class PredPanel(tk.Frame):
    def __init__(self, master=None, datadist=None):
        super().__init__(master)
        self.master = master
        self.datadist = datadist

        self.dist_contents = None
        self.vel_contents = None

        self.create_buttons()
        self.create_entries()
        self.create_outputs()
    
    def create_buttons(self):
        self.get_pred_button = tk.Button(self)
        self.get_pred_button["text"] = "Predict"
        self.get_pred_button["command"] = self.get_prediction
        self.get_pred_button.pack(side="bottom")

    def create_entries(self):

        self.vel_entry = tk.Entry(self)
        self.vel_entry.pack()
        
        # Create the velocity variable.
        self.vel_contents = tk.StringVar()
        # Set it to some value.
        self.vel_contents.set("Enter Velocity")
        # Tell the entry widget to watch this variable.
        self.vel_entry["textvariable"] = self.vel_contents

        self.dist_entry = tk.Entry(self)
        self.dist_entry.pack()

        # Create the distance variable.
        self.dist_contents = tk.StringVar()
        # Set it to some value.
        self.dist_contents.set("Enter Distance")
        # Tell the entry widget to watch this variable.
        self.dist_entry["textvariable"] = self.dist_contents
    
    def create_outputs(self):
        self.prediction_frame = tk.LabelFrame(self, text="Predicted Value", padx=5, pady=5)
        self.prediction_frame.pack(side=tk.BOTTOM)

        self.prediction = tk.Label(self.prediction_frame)
        self.prediction.pack(side=tk.BOTTOM)

    def predict_model(self, X):

        return self.datadist.model.predict(np.array(X).reshape(-1, 1))
    
    def plot_prediction(self, x, y):

        self.datadist.ax.scatter([x], [y])
        
        self.datadist.plot_canvas.draw()

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