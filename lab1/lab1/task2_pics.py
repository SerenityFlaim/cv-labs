import cv2 as cv

file_path_1 = "/home/serenity-flaim/Desktop/CV/lab1/media/anapa.jpg"
file_path_2 = "/home/serenity-flaim/Desktop/CV/lab1/media/one_word.png"
file_path_3 = "/home/serenity-flaim/Desktop/CV/lab1/media/december.jpeg"

img1 = cv.imread(file_path_1, cv.IMREAD_COLOR)
img2 = cv.imread(file_path_2, cv.IMREAD_ANYCOLOR)
img3 = cv.imread(file_path_3, cv.IMREAD_GRAYSCALE)
cv.namedWindow("DisplayWindow1", cv.WINDOW_NORMAL)
cv.namedWindow("DisplayWindow2", cv.WINDOW_AUTOSIZE)
cv.namedWindow("DisplayWindow3", cv.WINDOW_FULLSCREEN)


cv.imshow("DisplayWindow1", img1)
cv.imshow("DisplayWindow2", img2)
cv.imshow("DisplayWindow3", img3)
cv.waitKey(0)
cv.destroyAllWindows()