import csv
import operator
import cv2
import os
import pytesseract
import numpy as np
from datetime import date
from tkinter import *
from tkinter import filedialog

def Extract_Text(imageName,len,w1,w2,w3,w4):
    
    try:
        print(f"\t\tStarting the Extraction Process For the {len} Image ..........")
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
        img = cv2.imread(imageName)
        dimensions = img.shape
        print(dimensions);
        width, height = 400, 500
        pts1 = np.float32([[w1,w2], [w3,w2], [w1,w4], [w3,w4]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        gray = cv2.cvtColor(imgOutput, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray Image",imgOutput)
        # Performing OTSU threshold
        ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

        # Applying dilation on the threshold image

        dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

        # finding the contours
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

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
    sample = open('first.csv','r')
    csv1 = csv.reader(sample,delimiter=',')
    sort = sorted(csv1,key = operator.itemgetter(0))
    size = len(sort)
    with open('first.csv','w') as fd:
        for x in range(len(sort)):
            for y in sort[x]:
                fd.write(y+",")
            fd.write("\n")
def CpyToFinal(path,File_name):
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



imagename = "screen1.png";
# w1,w2,w3,w4 = 1484,166,1840,1024;
# print(w1,w2,w3,w4);

Extract_Text(imagename,1,1484,166,1840,1024)
RmNewLine()
Sorting_of_file()
CpyToFinal("C:\\Users\\hp\\Desktop\\MY COMPUTER\\python\\OpenCV Projects\\Zoom Attendance Assistant","file_name")
rmfirst()