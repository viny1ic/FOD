import cv2
import numpy as np
import time
import serial
from playsound import playsound

url = "http://192.168.2.3:8080" + "/video" # Your url might be different, check the app
webcam = cv2.VideoCapture(url)
# webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_BUFFERSIZE,3)

port = '/dev/ttyACM0'
arduino = serial.Serial(port, 9600)



def detect(img1, img2):
    blur1 = cv2.blur(img1,(10,10))
    blur2 = cv2.blur(img2,(10,10))
    img1_gray = cv2.cvtColor(blur1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(blur2, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(img1_gray, img2_gray)
    
    # _=diff[diff[:,:]>20].shape[0]

    print("diff = ", diff[diff[:,:]>20].shape[0])

    cv2.imshow("diff",diff)
    cv2.waitKey(2)
    
    return diff[diff[:,:]>50].shape[0] >100




def main():
    time.sleep(3)
    _,img2 = webcam.read()
    arduino.write('1'.encode())
    while True:     
        # while(arduino.in_waiting==0):
        #     img1=img2
        #     _,img2 = webcam.read()
        #     print("drain", end ='')
        print(arduino.readline().decode()[:-1])

        if True:
            img1=img2
            _,img2 = webcam.read()
            # _ = arduino.readline()
            if detect(img1, img2): #figure out a way to stop the arduino at this position
                print("Suspicious")
                for j in range(600):
                    _,img2 = webcam.read()
                    if not detect(img1, img2):
                        print("Not detected")
                        break
                if j==599:
                    print("confirmed")
                    while cv2.waitKey(1) & 0xff != ord('q'):
                        playsound("salamisound-4208277-smoke-detector-3-x-beeps.mp3")
                    break
            
            arduino.write('1'.encode())
            # arduino.reset_input_buffer()
            print("detecting")

if __name__=="__main__":
    main()
