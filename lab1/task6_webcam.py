import cv2 as cv
import numpy as np

def take_selfie():
    cap = cv.VideoCapture(0)
    ok, img = cap.read()
    if ok:
        cv.imwrite("media/webcam_selfie.jpg", img)

    cap.release()
    cv.destroyAllWindows()
    
#take_selfie()

file_path = "/home/serenity-flaim/Desktop/CV/lab1/media/webcam_selfie.jpg"
img = cv.imread(file_path, cv.IMREAD_COLOR)

def draw_rectangle(offset_x, offset_y, color=(0, 0, 255), thickness=3):
    h, w = img.shape[:2]
    center_x = w//2
    center_y = h//2
    x1 = center_x - offset_x
    y1 = center_y - offset_y
    x2 = center_x + offset_x
    y2 = center_y + offset_y
    cv.rectangle(img, (x1, y1), (x2, y2), color, thickness)

draw_rectangle(150, 50)
draw_rectangle(50, 150)
cv.namedWindow("cross", cv.WINDOW_AUTOSIZE)
cv.imshow("cross", img)
cv.waitKey(0)
cv.destroyAllWindows()