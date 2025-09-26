import cv2 as cv

file_path = "/home/serenity-flaim/Desktop/CV/lab1/media/redcurrant.jpg"

img = cv.imread(file_path, cv.IMREAD_COLOR)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.namedWindow("Origin Picture", cv.WINDOW_AUTOSIZE)
cv.namedWindow("HSV Picture", cv.WINDOW_AUTOSIZE)

cv.imshow("Origin Picture", img)
cv.imshow("HSV Picture", hsv_img)

cv.waitKey(0)
cv.destroyAllWindows()