class DataDistributor():

    def __init__(self):
        '''
            object that is used to share data with the rest of the
            modules.

            Contains:
                csv data
                model object
                plot variables

                definition for dependent and independent var strings
        '''
        # Data is a dictionary of lists, with column headers as keys
        self.data = None
        self.model = None
        self.ax = None
        self.figure1 = None
        self.plot_canvas = None

        # csv PARAMETERS
        self.DEPVAR_indicator = "DEPVAR"
        self.INDEPVAR_indicator = "INDEP"

        self.DEPVAR = None
        self.INDEPVAR = None

    def get_vars(self):
        ''' function to get column headers that correspond to
            dependant and independant variables

            None -> bool

            Returns 1 if csv has proper variables
            Inplace operation

            updates the depvar and indepvar lists with column headers
        '''
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
