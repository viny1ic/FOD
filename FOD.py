import cv2
import numpy as np


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
    if ans>1000:
        print("detected")
    else:
        print("not detected")


img1 = cv2.imread("try1.jpeg")
img2 = cv2.imread("try2.jpeg")
detect(img1, img2)
