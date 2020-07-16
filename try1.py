import cv2
import numpy as np
import time
from playsound import playsound

url = "http://192.168.2.2:8080" # Your url might be different, check the app
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(url+"/video")
# webcam = cv2.VideoCapture(0)

fpsLimit = 7 # throttle limit


def detect(img1, img2):
    # blur1 = cv2.GaussianBlur(img1 ,(7,7),cv2.BORDER_DEFAULT)
    # blur2 = cv2.GaussianBlur(img2 ,(7,7),cv2.BORDER_DEFAULT)
    blur1 = cv2.medianBlur(img1,15)
    blur2 = cv2.medianBlur(img2,15)
    img1_gray = cv2.cvtColor(blur1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(blur2, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(blur1, blur2)
    # mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    th = 40
    imask =  diff>th

    canvas = np.zeros_like(img2, np.uint8)
    canvas[imask] = img2[imask]

    cv2.imwrite("result.jpeg", canvas)
    result = cv2.imread("result.jpeg")
    a = np.asarray(result)
    a = a.tolist()
    ans=0
    # a.sort()
    # print(a)
    # ls=list()
    for i in a:
        for j in i:
            for k in j:
                # ls.append(k)
                if k>100:
                    ans+=1

    print(ans)

    if ans>100:
        return True
    else:
        return False

def grab(n):
        ret, img = webcam.read()
        cv2.imshow("capture",img)
        cv2.imwrite("img_"+str(n)+".jpg", img)
        cv2.waitKey(1)


startTime = time.time()
i=0
grab(i)
i+=1
while True:
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