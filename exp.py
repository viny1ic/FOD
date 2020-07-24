import cv2
import numpy as np
import time
from playsound import playsound

#url = "http://192.168.2.2:8080" # Your url might be different, check the app
#key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
# webcam = cv2.VideoCapture(0)
#webcam.set(cv2.CAP_PROP_BUFFERSIZE,1)

fpsLimit = 0.5 # throttle limit


def detect(img1, img2):
    blur1 = cv2.medianBlur(img1,15)
    blur2 = cv2.medianBlur(img2,15)
    img1_gray = cv2.cvtColor(blur1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(blur2, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(img1_gray, img2_gray)
    imask =  diff>100
    print(np.sum(np.reshape(imask,(-1))))

    return np.sum(np.reshape(imask,(-1)))>1000

def grab(n):
        ret, img = webcam.read()
        cv2.imshow("capture",img)
        cv2.imwrite("img_"+str(n)+".jpg", img)
        cv2.waitKey(1)
        # time.sleep(0.5)


startTime = time.time()
i=0
grab(i)
i+=1

while True:
    iterStart=time.time()
    grab(i)    
    nowTime = time.time()
    if (nowTime - startTime) > fpsLimit:
    
        img1 = cv2.imread("img_"+str(i)+".jpg")
        img2 = cv2.imread("img_"+str(i-1)+".jpg")
        if detect(img1, img2)==True:
            print("Suspicious")
            reference=i-1
            imgr = cv2.imread("img_"+str(reference)+".jpg")
            i+=1
            for j in range(7):
                grab(i)
                img2 = cv2.imread("img_"+str(i)+".jpg")
                if detect(imgr, img2)==False:
                    print("Not detected")
                    break
                i+=1
            if j==6:
                print("confirmed")
                playsound("salamisound-4208277-smoke-detector-3-x-beeps.mp3")
                break
        i+=1
        startTime = time.time()
        print(time.time()-iterStart)