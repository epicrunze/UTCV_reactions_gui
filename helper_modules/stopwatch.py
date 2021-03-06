#From https://code.activestate.com/recipes/124894-stopwatch-in-tkinter/
import time
import tkinter as tk
from tkinter import *

class Stopwatch(tk.Frame):
    def __init__(self, master=None, **kw):
        '''
        A class that packs a stopwatch into the GUI with a start, stop, and reset button.
        '''
        super().__init__(master)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()               
        self.makeWidgets()
        self.pack()
        self.create_buttons()
    
    def create_buttons(self):
        '''
        A function that packs the start, stop, and reset button into the GUI.
        '''
        self.start_button = tk.Button(self)
        self.start_button["text"] = "Start"
        self.start_button["command"] = self.Start
        self.start_button.pack()

        self.stop_button = tk.Button(self)
        self.stop_button["text"] = "Stop"
        self.stop_button["command"] = self.Stop
        self.stop_button.pack()

        self.reset_button = tk.Button(self)
        self.reset_button["text"] = "Reset"
        self.reset_button["command"] = self.Reset
        self.reset_button.pack()

    def makeWidgets(self):                         
        """ 
        A function that makes the time label. 
        """
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=2, padx=2)

    def _update(self): 
        """ 
        A function that updates the label with elapsed time. 
        """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
    
    def _setTime(self, elap):
        """
        A function that sets the time string to Minutes:Seconds:Hundreths 
        Keyword arguments:
        elap -- a floating-point number of the seconds elapsed since Start has been called.
        """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
        
    def Start(self):                                                     
        """ 
        A function that starts the stopwatch and ignores if already running. 
        """
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1        
    
    def Stop(self):                                    
        """
        A function that stops the stopwatch and ignores if already stopped.
        """
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0
    
    def Reset(self):                                  
        """ 
        A function that resets the stopwatch to 00:00:00
        """
        self._start = time.time()         
        self._elapsedtime = 0.0    
        self._setTime(self._elapsedtime)


if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(master=root)
    app.mainloop()
