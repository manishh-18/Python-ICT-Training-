import tkinter as tk
from tkinter import PhotoImage

# create the main window
root = tk.Tk()
root.title("Hello, this is my page using tkinter")
root.geometry("600x500")

# Used to show icon 
icon = PhotoImage(file='download.png')
root.iconphoto(True,icon)

# Run the main event loop it starts the main loop of the GUI ans it is responsible for handling all the events and updates written wihtin the application
root.mainloop() # This will be the last line 
