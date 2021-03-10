# UTCV_reactions_gui
A GUI for UTCV Reactions to lessen the time taken at competition.  

Written by: Ryan Zhang, Mackenzie Gole, Olevia Pal

## Running the GUI



    python newGUI.py 

this will start the GUI

### To install dependencies


run 

    pip install -r requirements.txt

## Description of each button


### Select csv to load


- Opens up a file dialog in your operating system
- User selects a csv file that they would like to use as data
- Loads the data into the GUI, and graphs it

### Start
- Activates stopwatch on the GUI
- Time recorded as hh:ss:msms
- Does not perform action if stopwatch is already running

### Stop
- Stops the stopwatch
- Does not perform action if stopwatch has not been started

### Reset
- Resets the stopwatch to 00:00:00
- Can be used when timer is running or stopped

### Predict
- Uses entries from "Enter Velocity" and "Enter Distance", returns a volume of reagent to use (in mL), based upon the chosen regression model.
- Time (s) is calculated through t = s/v 
- Volume of reagent is found through evaluating the chosen regression model at the calculated time

### Drop Down Menu 
- Allows the user to choose which type of model they would like to fit against the given data.
- The following models can be chosen:
    - #### _Linear_: Fits the data with a line, with a slope and intercept of the model. 
    - #### _RIReLU_: Fits the data with a model that generates random ReLU features for every input dimension.
    - #### _Polyfit_: Fits the data with a polynomial function of any degree. 
    - #### _Expofit_: Fits the data with a exponential function. 

### Create Model
- Click this button after the user selects a CSV to load, and a model from the drop down menu 
- Will fit the data, display the equation of the model, and the score of the function. 

### Clear
- After the CSV file is uploaded and fitted, if a different model or set of data is required, press this button.
- This will clear the graph displayed on the interface, as well as equations and scores. 

### Quit
- Allows the user to quit the GUI, clicking this button will close the window.  
