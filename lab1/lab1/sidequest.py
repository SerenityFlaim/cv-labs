import cv2 as cv
import numpy as np
file_path = "/home/serenity-flaim/Desktop/CV/lab1/media/december.jpeg"
img = cv.imread(file_path, cv.IMREAD_COLOR)

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

h, w = img.shape[:2]
print(h)
print(w)
center_x = w//2
center_y = h//2

def draw_rectangle(offset_x, offset_y, color=(0, 0, 255), thickness=3):
    x1 = center_x - offset_x
    y1 = center_y - offset_y
    x2 = center_x + offset_x
    y2 = center_y + offset_y
    cv.rectangle(img, (x1, y1), (x2, y2), color, thickness)

def draw_circle(radius, color, border):
    cv.circle(img,(center_x, center_y), radius, color, border)

for w_px in range(w):
    for h_px in range(h):
        if not(((h_px - center_x)**2 + (w_px - center_y)**2) < 350**2):
            img[h_px, w_px] = (255, 255, 255)


dominant_color = get_dominant_color(img[center_x, center_y])
draw_circle(350, dominant_color, 5)
draw_rectangle(350, 5, dominant_color, -1)
draw_rectangle(5, 350, dominant_color, -1)
cv.namedWindow("img", cv.WINDOW_NORMAL)
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()