#import tk library and ttk to style the widget
import tkinter as tk
from tkinter import ttk

#create function for the event
def onSelect(event):

    #create variable that gets the items selected and prints it
    selectedItem = event.widget.get()
    print("Selected item:", selectedItem)

#create root window
root = tk.Tk()
root.title("Combobox Example")