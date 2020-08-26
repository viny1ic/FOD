import cv2
import numpy as np
import time
import serial
from playsound import playsound

url = "http://192.168.2.3:8080" + "/video" # Your url might be different, check the app
webcam = cv2.VideoCapture(url)
# webcam = cv2.VideoCapture(0)
# webcam.set(cv2.CAP_PROP_BUFFERSIZE,1)

# fpsLimit = 0.5 # throttle limit

port = '/dev/ttyACM0'
arduino = serial.Serial(port, 9600)


def detect(img1, img2):
    blur1 = cv2.blur(img1,(10,10))
    blur2 = cv2.blur(img2,(10,10))
    img1_gray = cv2.cvtColor(blur1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(blur2, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(img1_gray, img2_gray)
    # _=diff[diff[:,:]>20].shape[0]

    # print("diff = ", diff[diff[:,:]>20].shape[0])

    # cv2.imshow("diff",diff)
    
    return diff[diff[:,:]>20].shape[0] >100




def main(): 
    _,img2 = webcam.read()

    while True:     
        while(arduino.in_waiting==0):
            img1=img2
            _,img2 = webcam.read()
            print("drain", end ='')
        if arduino.in_waiting>0:
            
            img1=img2
            _,img2 = webcam.read()
            if detect(img1, img2): #figure out a way to stop the arduino at this position
                print("Suspicious")
                for j in range(200):
                    _,img2 = webcam.read()
                    if not detect(img1, img2):
                        print("Not detected")
                        # arduino.write(1)
                        break
                if j==199:
                    print("confirmed")
                    playsound("salamisound-4208277-smoke-detector-3-x-beeps.mp3")
                    break
            arduino.reset_input_buffer()

if __name__=="__main__":
    main()
