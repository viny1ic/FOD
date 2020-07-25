import cv2
import numpy as np
import time
from playsound import playsound

url = "http://192.168.2.2:8080" + "/video" # Your url might be different, check the app
# webcam = cv2.VideoCapture(url)
webcam = cv2.VideoCapture(0)
# webcam.set(cv2.CAP_PROP_BUFFERSIZE,1)

# fpsLimit = 0.5 # throttle limit


def detect(img1, img2):
    # iterStart=time.time()
    blur1 = cv2.blur(img1,(10,10))
    blur2 = cv2.blur(img2,(10,10))
    img1_gray = cv2.cvtColor(blur1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(blur2, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(img1_gray, img2_gray)
    imask =  diff>20
    print(np.sum(np.reshape(imask,(-1))))
    condition=np.sum(np.reshape(imask,(-1)))>100
    # print("time taken to detect: ", time.time()-iterStart)
    # cv2.imshow("result", diff)
    return condition

def grab():
    # iterStart=time.time()
    ret, img = webcam.read()
    # cv2.imshow("capture",img)
    # cv2.imwrite("img_"+str(n)+".jpg", img)
    # cv2.waitKey(1)
    # print("time taken to grab: ", time.time()-iterStart)
    # time.sleep(0.5)
    return img


# startTime = time.time()
def main():
    img2=grab()

    while True:
        iterStart=time.time()
        img1=img2    
        # nowTime = time.time()
        # if (nowTime - startTime) > fpsLimit:
        
        # img1 = grab()
        img2 = grab()
        if detect(img1, img2):
            print("Suspicious")
            # reference=img1
            # imgr = grab()
            for j in range(100):
                img2=grab()
                # img2 = cv2.imread("img_"+str(i)+".jpg")
                if not detect(img1, img2):
                    print("Not detected")
                    break
            if j==99:
                print("confirmed")
                playsound("salamisound-4208277-smoke-detector-3-x-beeps.mp3")
                break
        startTime = time.time()
        print(time.time()-iterStart)

if __name__=="__main__":
    main()
