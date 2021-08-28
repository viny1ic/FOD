import cv2 # LIBRARY FOR IMAGE RECOGNITION AND PROCESSING
import numpy as np # LIBRARY FOR MATRIX MANIPULATION
import time
import serial # LIBRARY FOR COMMUNICATION WITH ARDUINO
from playsound import playsound # LIBRARY TO PLAY SOUND

# SET THE VIDEO FEED SOURCE
url = "http://192.168.2.3:8080" + "/video" 

# SET INTEGER INSTEAD OF 'url' IF USING WIRED USB CAMERA
webcam = cv2.VideoCapture(url)

# COMMENT OUT IF FACING LAG ISSUES
webcam.set(cv2.CAP_PROP_BUFFERSIZE,3)

# SET ARDUINO PORT (DIFFERENT FOR DIFFERENT DEVICES)
port = '/dev/ttyACM0'
arduino = serial.Serial(port, 9600)


# THIS IS THE MOST IMPORTANT FUNCITON OF THE PROJECT.
# THIS FUNCTION DETECTS THE DIFFERENCE BETWEEN TWO IMAGES
def detect(img1, img2):

    # IMAGE BLURRING IN ORDER TO MAKE THE DIFFERENTIATION SMOOTHER
    blur1 = cv2.blur(img1,(10,10))
    blur2 = cv2.blur(img2,(10,10))

    # CONVERTING IMAGES FROM BGR TO GRAYSCALE
    img1_gray = cv2.cvtColor(blur1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(blur2, cv2.COLOR_BGR2GRAY)

    # CALCULATE DIFFERENCES BETWEEN THE TWO IMAGE ARRAYS
    diff = cv2.absdiff(img1_gray, img2_gray)

    # SHOW THE DIFFERENCE BETWEEN THE TWO IMAGES
    cv2.imshow("diff",diff)
    cv2.waitKey(2)

    # RETURN THE DIFFERENCE OF THE TWO IMAGES
    # ADJUST THESE VALUES TO CHANGE THE SENSITIVITY OF DETECTION
    return diff[diff[:,:]>50].shape[0] >200




def main():

    # DELAY TO COMPLETE SERIAL CONNECTION WITH ARDUINO
    time.sleep(3)
    arduino.write('1'.encode())
    first_30 = True
    first_60 = True
    while True:
        # READ CAMERA INPUT IF NO MESSEGES IN WAITING FOR ARDUINO SERIAL  
        if(arduino.in_waiting==0):
            _,_ = webcam.read()

        # IF SERIAL INPUT FROM ARDUINO EXISTS, READ IT
        else:
            pos = int(arduino.readline().decode()[:-1])
            print(pos)
            
            # HANDLE IMAGES AT THE 30 DEGREE X ANGLE
            if pos == 30:
                # IF READING THIS ANGLE FOR THE FIRST TIME, JUST READ IMAGE AND CONTINUE
                if first_30:
                    arduino.write('1'.encode())
                    _,img_30_2 = webcam.read()
                    first_30=False
                    print(first_30)
                    continue
                # TIME CALCULATION FOR DEBUGGING. COMMENT OUT WHILE ACTUALLY RUNNING
                t1 = time.time()

                # DETECT DIFFERENCE BETWEEN TWO IMAGES
                img_30_1=img_30_2
                _,img_30_2 = webcam.read()

                # IF DIFFERENCE IS DETECTED, ENTER THE SUSPICIOUS LOOP AND EXAMINE FOR 200 ITERATIONS
                if detect(img_30_1, img_30_2):
                    print("Suspicious")

                    # CHANGE THIS VALUE TO INCREASE THE SUSPICIOUS EXAMINATION TIME
                    for j in range(200):
                        _,img_30_2 = webcam.read()
                        if not detect(img_30_1, img_30_2):
                            print("Not detected")
                            break

                    # IF DIFFERENCE STILL EXISTS AFTER GIVEN SUSPICIOUS EXAMINATION TIME, SOUND ALARM
                    if j==199:
                        print("confirmed")
                        while cv2.waitKey(1) & 0xff != ord('q'):
                            playsound("salamisound-4208277-smoke-detector-3-x-beeps.mp3")
                        break                
                print("detecting")

                # TIME CALCULATION FOR DEBUGGING. COMMENT OUT WHILE ACTUALLY RUNNING
                print(time.time()-t1)


            if pos == 60:
                # IF READING THIS ANGLE FOR THE FIRST TIME, JUST READ IMAGE AND CONTINUE
                if first_60:
                    arduino.write('1'.encode())
                    _,img_60_2 = webcam.read()
                    first_60=False
                    print(first_60)
                    continue

                # TIME CALCULATION FOR DEBUGGING. COMMENT OUT WHILE ACTUALLY RUNNING
                t1 = time.time()

                # DETECT DIFFERENCE BETWEEN TWO IMAGES
                img_60_1=img_60_2
                _,img_60_2 = webcam.read()

                # IF DIFFERENCE IS DETECTED, ENTER THE SUSPICIOUS LOOP AND EXAMINE FOR 200 ITERATIONS
                if detect(img_60_1, img_60_2):
                    print("Suspicious")
                    
                    # CHANGE THIS VALUE TO INCREASE THE SUSPICIOUS EXAMINATION TIME
                    for j in range(200):
                        _,img_60_2 = webcam.read()
                        if not detect(img_60_1, img_60_2):
                            print("Not detected")
                            break
                        
                    # IF DIFFERENCE STILL EXISTS AFTER GIVEN SUSPICIOUS EXAMINATION TIME, SOUND ALARM
                    if j==199:
                        print("confirmed")
                        while cv2.waitKey(1) & 0xff != ord('q'):
                            playsound("salamisound-4208277-smoke-detector-3-x-beeps.mp3")
                        break              
                print("detecting")

                # TIME CALCULATION FOR DEBUGGING. COMMENT OUT WHILE ACTUALLY RUNNING
                print(time.time()-t1)
            
            # DRAIN CAMERA BUFFER WHILE CAMERA IS MOVING TO ELIMINATE LAG
            else:
                _,_ = webcam.read()
            arduino.write('1'.encode())
        

if __name__=="__main__":
    main()
