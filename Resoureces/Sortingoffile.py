# Import Tkinter library
from tkinter import *

# Create an instance of tkinter frame
window0 = Tk()

# Set the geometry of Tkinter frame
window0.geometry("700x250")

# Define Function to print the input value
def get_choice():
   global vv1;
   global vv2;
   vv1 = vvar1.get()
   vv2 = vvar2.get()
   print("Input for Create:", vvar1.get())
   print("Input for Append:", vvar2.get())
   print("Input variable for Create:", vv1)
   print("Input variable for Append:", vv2)

# Define empty variables
vvar1 = IntVar()
vvar2 = IntVar()

# Define a Checkbox
t1 = Checkbutton(window0,bg = "#F2A467", text="Create File", variable=vvar1, onvalue=1, offvalue=0, command=get_choice).place(x = 50,y = 75)
t2 = Checkbutton(window0,bg = "#F2A467", text="Add to existing file", variable=vvar2, onvalue=1, offvalue=0, command=get_choice).place(x = 50,y = 104)

window0.mainloop()