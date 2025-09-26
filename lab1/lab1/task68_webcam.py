import cv2 as cv
import numpy as np

def take_selfie():
    cap = cv.VideoCapture(0)
    ok, img = cap.read()
    if ok:
        cv.imwrite("media/webcam_selfie2.jpg", img)

    cap.release()
    cv.destroyAllWindows()
    
take_selfie()



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

def get_dominant_color(center_pixel):
    b, g, r = center_pixel.astype(np.int32)
    dist_to_red = np.sqrt((r - 255)**2 + (g - 0)**2 + (b - 0)**2)
    dist_to_green = np.sqrt((r - 0)**2 + (g - 255)**2 + (b - 0)**2)
    dist_to_blue = np.sqrt((r - 0)**2 + (g - 0)**2 + (b - 255)**2)
    distances = [dist_to_red, dist_to_green, dist_to_blue]
    min_dist = min(distances)

    if min_dist == dist_to_red:
        return (0, 0, 255)
    elif min_dist == dist_to_green:
        return (0, 255, 0)
    else:
        return (255, 0, 0)


cap = cv.VideoCapture(0)
ok, img = cap.read()
while True:
    ok, img = cap.read()
    if not ok:
        break
    h, w = img.shape[:2]
    center_x = w//2
    center_y = h//2
    get_dominant_color(img[center_x, center_y])
    draw_rectangle(150, 50, get_dominant_color(img[center_x, center_y]), -1)
    draw_rectangle(50, 150, get_dominant_color(img[center_x, center_y]), -1)
    cv.imshow('img', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    


h, w = img.shape[:2]
center_x = w//2
center_y = h//2
print(get_dominant_color(img[center_x, center_y]))
draw_rectangle(150, 50, get_dominant_color(img[center_x, center_y]), -1)
draw_rectangle(50, 150, get_dominant_color(img[center_x, center_y]), -1)



cv.namedWindow("cross", cv.WINDOW_AUTOSIZE)
cv.imshow("cross", img)
cv.waitKey(0)
cv.destroyAllWindows()