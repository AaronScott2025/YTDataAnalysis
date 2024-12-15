import tkinter as tk
import pandas as pd
import json as js
import os
import matplotlib

class GUI:
    ##
    # __init__()
    # Initializes and opens the window.
    #
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("YT Trend Analysis")
        self.window.geometry("1200x900")

    ##
    #run()
    #runs GUI
    #
    def run(self):
        self.window.mainloop()



if __name__ == '__main__':
    app = GUI()
    app.run()