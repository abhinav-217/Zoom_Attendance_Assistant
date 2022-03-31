from tkinter import filedialog as fd
import os
filename = fd.askopenfilename()

print(filename);

file = os.path.basename(filename);
print(file)