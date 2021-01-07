# code for data intake widget
class DataIntake(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.create_buttons()

    def create_buttons(self):
        self.load_csv = tk.Button(self)
        self.load_csv["text"] = "Select csv to Load"
        self.load_csv["command"] = self.read_csv
        self.load_csv.pack(side="left")

    def read_csv(self):
        # csv or similar file with DEPVAR column, and TIME column
        filename = tk.filedialog.askopenfilename()
        
        # read csv as pandas df, then convert to dictionary
        self.data = pd.read_csv(filename).to_dict(orient="list")

        self.plot_csv()