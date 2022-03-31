import csv
import operator
import cv2
import os
import pytesseract
import numpy as np
from datetime import date
from tkinter import *
from tkinter import filedialog


def Extract_Text(imageName, len, w1, w2, w3, w4):

    try:
        print(
            f"\t\tStarting the Extraction Process For the {len} Image ..........")
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
        img = cv2.imread(imageName)
        # dimensions = img.shape
        # print(dimensions);
        width, height = 400, 500
        pts1 = np.float32([[w1, w2], [w3, w2], [w1, w4], [w3, w4]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        gray = cv2.cvtColor(imgOutput, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray Image", imgOutput)
        # Performing OTSU threshold
        ret, thresh1 = cv2.threshold(
            gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

        # Applying dilation on the threshold image

        dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

        # finding the contours
        contours, hierarchy = cv2.findContours(
            dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        im2 = imgOutput.copy()
        file = open("first.csv", "w+")
        file.write("")
        file.close()

        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cropped = im2[y:y + h, x:x + w]
            file = open("first.csv", "a")
            text = pytesseract.image_to_string(cropped)
            file.write(text)
            file.write("\n")
    except:
        print("\n\n")


def RmNewLine():
    with open('first.csv', 'r+') as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()


def Sorting_of_file():
    sample = open('first.csv', 'r')
    csv1 = csv.reader(sample, delimiter=',')
    sort = sorted(csv1, key=operator.itemgetter(0))
    size = len(sort)
    with open('first.csv', 'w') as fd:
        for x in range(len(sort)):
            for y in sort[x]:
                # fd.write(y+",")
                fd.write(y)
            fd.write("\n")


def CpyToFinal(path, File_name):
    today = date.today()
    fileName = File_name
    save_path = path
    name_of_file = fileName
    completeName = os.path.join(save_path, name_of_file+".csv")
    with open('first.csv', 'r') as firstfile, open(completeName, 'a') as secondfile:

        for line in firstfile:
            secondfile.write(line.rstrip('\n') + ",         P" + '\n')


def rmfirst():
    os.remove("first.csv")



def OpenNext():
    window0.destroy()
    if vv1 == 1:
        window = Tk()
        window.geometry("500x450")
        window.config(background="#0B0260")
        window.title(
            "                                        Zoom Attendance Assistant")
        window.minsize(500, 450)
        window.maxsize(500, 450)

        def browseFiles():
            window.filename = filedialog.askopenfilenames(initialdir="C:\\",
                                                          title="Select a File",
                                                          filetypes=(("Image files",
                                                                      "*.png*"),
                                                                     ("Image files",
                                                                      "*.jpeg*"), ("Image files", "*.jpg"), ("Image files", "*.jfif")))
            global Imagefiles_Program
            Imagefiles_Program = window.filename

        def display_input1():
            global v1
            global v2
            v1 = var1.get()
            v2 = var2.get()

        def OpenDirectory():
            window.filename = filedialog.askdirectory()
            global folder_directory
            folder_directory = window.filename

        def getFileName():
            global file_name
            file_name = scvalue.get()
            scvalue.set("")

        # Creating the Welcome text
        Heading = Label(text=''' Zoom Attendance Assistant''',
                        bg="#E900FF", fg="white", font="Lucida 15 bold")
        Heading.pack(padx=30, pady=10, ipadx=20, ipady=20)
        var1 = IntVar()
        var2 = IntVar()
        # Check box for laptop android
        checkFrame = Frame(window, borderwidth=6, bg="#C9F3F0",
                           relief=SUNKEN).place(x=80, y=100)
        label = Label(checkFrame, text="Select The Screenshot type", bg="#C8F0AF",
                      padx=10, pady=10, font="Lucida 10 bold").place(x=93, y=105)
        t1 = Checkbutton(checkFrame, bg="#F2A467", text="Screenshot from Android**",
                         variable=var1, onvalue=1, offvalue=0, command=display_input1).place(x=93, y=149)
        t2 = Checkbutton(checkFrame, bg="#F2A467", text="Screenshot from Laptop/PC**",
                         variable=var2, onvalue=1, offvalue=0, command=display_input1).place(x=93, y=179)

        # File name box here
        scvalue = StringVar()
        scvalue.set(" ")
        file_name = StringVar()
        Filelabel = Label(window, text="Enter the File Name....",
                          bg="#C8F0AF").place(x=93, y=220)
        screen = Entry(window, textvariable=scvalue,
                       font="lucida 10 bold", width=20).place(x=93, y=245)
        ok_btn = Button(window, text="Save File Name",
                        command=getFileName).place(x=93, y=280)

        # Choose Directory Button
        btn1 = Button(window, text="Choose Directory\n For saving file**",
                      font="lucida 10 bold", command=OpenDirectory, padx=10, pady=1).place(x=93, y=330)

        # Frame for Upload done and cancel Button

        b1 = Button(window, bg="#F2A467", fg="Black", text="Upload\n the ScreenShot",
                    font="lucida 10 bold", command=browseFiles).place(x=253, y=330)
        b3 = Button(window, fg="red", bg="White", text="Done",
                    font="lucida 10 bold", command=window.destroy).place(x=93, y=390)
        b2 = Button(window, fg="red", bg="White", text="Cancel",
                    font="lucida 10 bold", command=exit).place(x=143, y=390)
        window.mainloop()
    elif vv1 == 0:
        root1 = Tk()
        root1.geometry("300x300")
        root1.config(bg="#FFFFE7")
        root1.title("it's a append to file")
        label1 = Label(root1, text="The work is going on this Function",
                       font="lucida 13 bold").place(x=5, y=50)
        root1.mainloop()


def get_choice():
    global vv1
    global vv2
    vv1 = vvar1.get()
    vv2 = vvar2.get()



def AppendFile():
    print("It's a Append")


window0 = Tk()
window0.geometry("300x300")
window0.config(bg="#FFFFE7")
lbl1 = Label(window0, text="Select the file type: ",
             font="lucida 10 bold", bg="black", fg="white").place(x=50, y=30)
vvar1 = IntVar()
vvar2 = IntVar()
t1 = Checkbutton(window0, bg="#F2A467", text="Create File", variable=vvar1,
                 onvalue=1, offvalue=0, command=get_choice).place(x=50, y=75)
t2 = Checkbutton(window0, bg="#F2A467", text="Add to existing file",
                 variable=vvar2, onvalue=1, offvalue=0, command=get_choice).place(x=50, y=104)

btn1 = Button(window0, text="Next", bg="aqua", fg="black",
              command=OpenNext).place(x=160, y=260)
btn2 = Button(window0, text="Cancel", bg="aqua",
              fg="black", command=exit).place(x=220, y=260)

window0.mainloop()
if vv1 ==1:
    win = Tk()
    win.geometry("400x200")
    win.config(background = "#0B0260")
    win.title("Zoom Attendance Assistant Pop-Up")
    Heading = Label(text = '''The Work Has Been Completed''',bg = "#E900FF",fg = "white",font="Lucida 10 bold")
    Heading.pack(padx=30,pady=10,ipadx=20,ipady=20)
    btn1 = Button(fg = "red",bg = "White",text = "Close Window",font = "lucida 9 bold",command = exit)
    btn1.pack(pady=40 , side=RIGHT,padx=35,ipady=2)
    btn1.config(bg="#F2A467", fg="black")
    filSave = Label(win,bg = "#FEA9A6",text = "*** The file is Saved\n At the selected location ***",padx=7,font = "lucida 8 bold").place(x = 78,y = 78)
    try:
        len_tup = len(Imagefiles_Program)
        path = str(folder_directory)
        for x in range(0,len_tup):
            if v1 ==1:
                Extract_Text(Imagefiles_Program[x],x+1,74,126,608,1458)
                RmNewLine()
                Sorting_of_file()
                CpyToFinal(path,file_name)
                rmfirst()
            elif v1 == 0:
                Extract_Text(Imagefiles_Program[x],x+1,1484,166,1840,1024)
                RmNewLine()
                Sorting_of_file()
                CpyToFinal(path,file_name)
                rmfirst()
            
               
    except:
        win2 = Tk()
        win2.geometry("350x500")
        win2.config(background = "#0B0260")
        win2.title("Error Window.....")
        label = Label(win2,text = '''Error....''',bg = "#0B0260",fg = "white",font="Lucida 15 bold")
        label.pack(pady=4,ipadx=10,ipady=10)
        
        label1 = Label(win2,text = '''****  1. The Path of the file may be wrong''',bg = "#0B0260",fg = "white",font="Lucida 10 bold")
        label1.pack(pady=4,ipadx=10,ipady=10)

        label2 = Label(win2,text = '''****  2. The File name could be Wrong''',bg = "#0B0260",fg = "white",font="Lucida 10 bold")
        label2.pack(pady=4,ipadx=10,ipady=10)

        label3 = Label(win2,text = '''****  3. The File has any special Characters''',bg = "#0B0260",fg = "white",font="Lucida 10 bold")
        label3.pack(pady=4,ipadx=10,ipady=10)

        label4 = Label(win2,text = '''****  4. The File name conataining the ( ) ''',bg = "#0B0260",fg = "white",font="Lucida 10 bold")
        label4.pack(pady=4,ipadx=10,ipady=10)

        label5 = Label(win2,text = '''****  5. The File Name consist of spaces in between''',bg = "#0B0260",fg = "white",font="Lucida 10 bold")
        label5.pack(pady=4,ipadx=10,ipady=10)

        label6 = Label(win2,text = '''****  6. The Path for saving the file was not selected''',bg = "#0B0260",fg = "white",font="Lucida 10 bold")
        label6.pack(pady=4,ipadx=10,ipady=10)

        label7 = Label(win2,text = '''****  7. The File was not Uploaded Correctly ''',bg = "#0B0260",fg = "white",font="Lucida 10 bold")
        label7.pack(pady=4,ipadx=10,ipady=10)
        
        label8 = Label(win2,text = '''****  8. The CheckBox was not selected ''',bg = "#0B0260",fg = "white",font="Lucida 10 bold")
        label8.pack(pady=4,ipadx=10,ipady=10)
        
        label9 = Label(win2,text = '''****  9. The Program Closed Accidentally ''',bg = "#0B0260",fg = "white",font="Lucida 10 bold")
        label9.pack(pady=4,ipadx=10,ipady=10)
        
        win2.mainloop()
    win.mainloop()
    
elif vv1==0:
    print("it's a append")
