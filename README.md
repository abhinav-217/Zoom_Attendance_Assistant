# Zoom_Attendance_Assistant
This is Zoom Attendance System that let you takes attendance of the people present in your zoom meeting through a screenshot

In our today's online age due to increasing covid cases, the college and the school are going on an online classes system in which Zoom Meeting Software is widely 
used. The marking of the attendance is very hectic work for the teachers or the host.
So here is the solution for that a Zoom Attendance Assistant which takes the attendance of the participants just by the screenshot of the participants' list in the 
zoom meeting app.
This Zoom Attendance Assistant works using the Computer Vision Library known as Opencv and the use of an OCR tool pytesseract which helps to extracts the text from 
the image so that we can further use it or manipulate it.
The Algorithm for the process is as follows:-

•	First, it will take the screenshot of the image and then we find the region of interest in the image that is the region where the participants list is present 
after locating the region of interest we then convert the image to warp perspective(an opencv function).

•	In the second step after the conversion to warp perspective, we then convert the image to grayscale as a grayscale image is better and fast for processing 
and we do not have any significance related to the colors present in the image.

•	After the Gray scaling of the image is done we perform the following steps (OTSU Threshold, Applying dilation to the threshold image, and then finding 
the contours) on it to make the image better for the recognizing of the text.

•	Now after the previous step we finally pass the image to the pytesseract module to recognize the text from the image.

•	After the recognition of the text from the image, the names of the participants are now transferred to the excel file in which they are marked as present 
and the file is saved as any custom name by your choice, also the file is alphabetically sorted.

•	Also, the program can work with screenshot from both mobile and pc though they have a different region of interest.

It was a great project for me to do and the intreseting one.

Hope You Liked it............😊😊🔥
