import cv2 as cv
def border_processor(img_path):
    img = cv.imread(img_path)
    img_grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_blurred = cv.GaussianBlur(img_grayscale, (5, 5), 1)

    cv.imshow("Original", img)
    cv.imshow("Grayscale|Blurred", img_blurred)

    cv.waitKey(0)
    cv.destroyAllWindows()

border_processor("/home/serenity-flaim/Desktop/CV/lab1/media/lab4/sonic_freedom.jpg")