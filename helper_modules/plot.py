import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class Plotter(tk.Frame):
    def __init__(self, master=None, datadist=None):
        super().__init__(master)
        self.master = master
        self.datadist = datadist
        self.pack()

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