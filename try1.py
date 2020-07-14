import cv2
import numpy as np
import time

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)


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
    ans=0
    for i in np.nditer(a):
        # print(i)
        if i>100:
            ans+=1
    print(ans)
    # time.sleep(1)
    if ans>1000:
        return True
    else:
        return False

def grab(n):
        ret, img = webcam.read()
        cv2.imshow("capture",img)
        cv2.imwrite("img_"+str(i)+".jpg", img)
        cv2.waitKey(1)
# detect(img1, img2)
i=0
grab(i)
i+=1
while True:
    grab(i)
    img1 = cv2.imread("img_"+str(i-1)+".jpg")
    img2 = cv2.imread("img_"+str(i)+".jpg")
    if detect(img1, img2)==True:
        print("Suspicious")
        i+=1
        for j in range(10):
            grab(i)
            img2 = cv2.imread("img_"+str(i)+".jpg")
            if detect(img1, img2)==False:
                print("Not detected")
                break
            i+=1
        if j==9:
            print("confirmed")
            break
    i+=1