from tkinter import *
import glob
import time

# Update interval for the application
update_interval = 2000

# Some system configuration reading
base_dir = "/sys/bus/w1/devices/"
device_folder = glob.glob(base_dir + "28*")[0]
device_file = device_folder + "/w1_slave"
# Read the raw temp reading from the file representing the sensor
# Helper function
def read_temp_raw():
    f = open(device_file, "r")
    lines = f.readlines()
    f.close()
    return lines


# Read the temperature, return as a float
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != "YES":
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find("t=")
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2 :]
        temp_c = float(temp_string) / 1000.0
        return temp_c
    else:
        return 0.00



# Set up the window
root = Tk()
root.geometry("360x240")
v = StringVar()
# This is a label, the temp goes here
l = Label(root, textvariable=v, font=("Helvetica", 128))
# ?
l.pack()


# Depending on the temperature, choose a color
def chooseColor(temp):
    if temp < 35:
        return "blue"
    elif temp < 37.2:
        return "orange"
    else:
        return "red"

# Function to update Temperature
def updateTemp():
    # Get temp
    temp = read_temp()
    msg = str(temp)
    # Set text color accordingly
    l.config(fg=chooseColor(temp))
    v.set(msg)
    # Run this again after update
    root.after(update_interval, updateTemp)

# Initial blank message
v.set("--.-")

root.after(update_interval, updateTemp)
# Run the app now
root.mainloop()