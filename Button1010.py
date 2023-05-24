#call on tkinter library
import tkinter as tk

#create function for when the button is clicked
def buttonClick():
    print("Button clicked!")

#create parent windown or root window
root = tk.Tk()
root.title("Button Example")

#create button with 3 paramaters the class library the text and the function call
button = tk.Button(root, text="YAYEET", command=buttonClick)
button.pack()

#create mainloop to keep root window open
root.mainloop()