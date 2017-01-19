# NAOColorTracker

##Introduction 
The Current project has been tested on the simulator located in  the folder NaoVisualChoregraphy/BUILD/ on linux 14.04.

##Guide

### Step 1
Run the ServerColorTracker.py script. Be aware that you will need OPENCV3 and Python 3.4.

### Step 2
Run the executable file NaoVisualChoregraphy/BUILD/TrackMultipleColor.x86_64.

### Step 3
Press the Start Button.

## Result
You will see that the python script receive the camera frame from the simulator, all the colored target are tracked.

##Tuning
You can tune your own color tracker by modifying the H value of the [Color]UpperBound and [Color]LowerBound variables. If you want to use real webcam you have to comment the TCP IP Simulation Part and the Simulator Part in the main loop.
Then you have to uncomment the two Webcam Part
