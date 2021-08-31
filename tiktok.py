import cv2
import time
import numpy as np
import cvzone


def tiktok(w, h, moveRight=True):
    cap = cv2.VideoCapture(0)
    cap.set(3, w)
    cap.set(4, h)

    zero = np.zeros((h, w, 3), np.uint8)
    lineRight = np.zeros((h, 2, 3), np.uint8)
    lineDown = np.zeros((2, w, 3), np.uint8)

    x = 0
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        time.sleep(0.005)
        x += 2
        if moveRight:
            zero[0:h, x:x+2] = img[0:h, x:x+2]
            if x < w-2:
                stackImages = cvzone.stackImages([zero[0:h, 0:x+2], lineRight, img[0:h, x+3:w]], 3, 1)
                cv2.imshow("Image", stackImages)
            cv2.waitKey(1)
        else:
            zero[x:x+2, 0:w] = img[x:x+2, 0:w]
            if x < h-2:
                stackImages = cvzone.stackImages([zero[0:x+2, 0:w], lineDown, img[x+3:h, 0:w]], 1, 1)
                cv2.imshow("Image", stackImages)
            cv2.waitKey(1)


tiktok(640, 480)


