import numpy as np
import cv2
import time


USB_PORT = "/dev/ttyUSB0"  # Arduino Uno WiFi Rev2
# Imports
import serial

try:
   usb = serial.Serial(USB_PORT, 9600, timeout=2)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit()

Known_distance = 76.2

Known_width = 14.3


GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


fonts = cv2.FONT_HERSHEY_COMPLEX

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def Focal_Length_Finder(measured_distance, real_width, width_in_rf_image):

	
	focal_length = (width_in_rf_image * measured_distance) / real_width
	return focal_length


def Distance_finder(Focal_Length, real_face_width, face_width_in_frame):

	distance = (real_face_width * Focal_Length)/face_width_in_frame

	
	return distance


def face_data(image):

	face_width = 0 

	
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	faces = face_detector.detectMultiScale(gray_image, 1.1, 5)

	for (x, y, h, w) in faces:

		cv2.rectangle(image, (x, y), (x+w, y+h), GREEN, 2)

		face_width = w


	return face_width


ref_image = cv2.imread("Ref_image.png")


ref_image_face_width = face_data(ref_image)

Focal_length_found = Focal_Length_Finder(
	Known_distance, Known_width, ref_image_face_width)

def coord(image):

    face_width = 0 

    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)

    for (x, y, h, w) in faces:

        cv2.rectangle(image, (x, y), (x+w, y+h), RED, 2)

        face_width = w

        print('x= ',x, "  y = ", y)
        
        """elif command == "a":  # turn off Arduino LED
          usb.write(b'3')  # send command to Arduino
          print("Arduino motor turned off.")
   elif command == "d":  # turn off Arduino LED
          usb.write(b'4') """


        if x<200:
            print('moving robot to the right')
            usb.write(b'3')
            time.sleep(2)

        elif x>300:
            
            print('moving robot to the left')
            usb.write(b'4')
            time.sleep(2)

        if y<100:
            
            print('moving camera down')

        elif y>300:
            
            print('moving camera up')


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    face_width_in_frame = face_data(frame)

    if face_width_in_frame != 0:
        Distance = Distance_finder(Focal_length_found, Known_width, face_width_in_frame)
        cv2.line(frame,(30,30),(230,30),RED,32)
        cv2.line(frame, (30, 30), (230, 30), BLACK, 28)
        cv2.putText(
			frame, f"Distance: {round(Distance,2)} CM", (30, 35),
		fonts, 0.6, GREEN, 2)
        #coord(frame)
        if(Distance<70 ):
            print("inapoi")
            usb.write(b'2')
            #time.sleep(0.4)
            
        elif(70<Distance<100):
            print("stop")
            usb.write(b'0')
            #time.sleep(0.4)
        elif(Distance>100):
            print("inainte")
            usb.write(b'1')
            #time.sleep(0.4)
        


    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()