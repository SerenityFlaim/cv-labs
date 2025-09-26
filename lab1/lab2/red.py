import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
ok, img = cap.read()

lower1 = np.array([0, 120, 70])
upper1 = np.array([10, 255, 255])
lower2 = np.array([170, 120, 70])
upper2 = np.array([179, 255, 255])

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))

while True:
    ok, img = cap.read()
    if not ok:
        break
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    mask1 = cv.inRange(hsv_img, lower1, upper1)
    mask2 = cv.inRange(hsv_img, lower2, upper2)
    mask = cv.bitwise_or(mask1, mask2)

    opening = cv.dilate(cv.erode(mask, kernel, iterations=1), kernel, iterations=1)
    closing = cv.erode(cv.dilate(mask, kernel, iterations=1), kernel, iterations=1)

    filter_img = cv.bitwise_and(img, img, mask=mask)
    open_img = cv.bitwise_and(img, img, mask=opening)
    close_img = cv.bitwise_and(img, img, mask=closing)
    
    cv.imshow('webcam', filter_img)
    cv.imshow('mask', mask)
    cv.imshow('opening', opening)
    cv.imshow('closing', closing)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()