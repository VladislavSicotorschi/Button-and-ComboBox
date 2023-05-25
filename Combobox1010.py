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

#create array list for items
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

#create combo box object and input values from items array
comboBox = ttk.Combobox(root, values=items)

#bind combo box object to the selector event
comboBox.bind("<<ComboboxSelected>>", onSelect)
