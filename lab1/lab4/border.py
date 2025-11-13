import cv2 as cv
import numpy as np

def get_grad_angle(gradient_x, gradient_y, tg):
    grad_angle = np.zeros_like(gradient_x, dtype=np.uint8)

    segment0 = ((gradient_x > 0) & (gradient_y < 0) & (tg < -2.414)) | ((gradient_x < 0) & (gradient_y < 0) & (tg > 2.414))
    grad_angle[segment0] = 0

    segment1 = (gradient_x > 0) & (gradient_y < 0) & (tg >= -2.414) & (tg < -0.414)
    grad_angle[segment1] = 1

    segment2 = ((gradient_x > 0) & (gradient_y < 0) & (tg >= -0.414)) | ((gradient_x > 0) & (gradient_y > 0) & (tg < 0.414))
    grad_angle[segment2] = 2

    segment3 = (gradient_x > 0) & (gradient_y > 0) & (tg >= 0.414) & (tg < 2.414)
    grad_angle[segment3] = 3

    segment4 = ((gradient_x > 0) & (gradient_y > 0) & (tg >= 2.414)) | ((gradient_x < 0) & (gradient_y > 0) & (tg <= -2.414))
    grad_angle[segment4] = 4

    segment5 = (gradient_x < 0) & (gradient_y > 0) & (tg > -2.414) & (tg <= -0.414)
    grad_angle[segment5] = 5

    segment6 = ((gradient_x < 0) & (gradient_y > 0) & (tg > -0.414)) | ((gradient_x < 0) & (gradient_y < 0) & (tg < 0.414))
    grad_angle[segment6] = 6

    segment7 = (gradient_x < 0) & (gradient_y < 0) & (tg >= 0.414) & (tg < 2.414)
    grad_angle[segment7] = 7

    return grad_angle


def border_processor(img_path):
    img = cv.imread(img_path)
    img_grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_blurred = cv.GaussianBlur(img_grayscale, (5, 5), 2)

    Gx = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=np.float64)

    Gy = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ], dtype=np.float64)

    gradient_x = np.zeros_like(img_blurred, dtype=np.float64)
    gradient_y = np.zeros_like(img_blurred, dtype=np.float64)

    padding = np.pad(img_blurred, ((1, 1), (1, 1)), mode='reflect')

    h, w = img_blurred.shape[:2]

    for i in range(h):
        for j in range(w):
            process_region = padding[i:i+3, j:j+3]
            gradient_x[i, j] = np.sum(process_region * Gx)
            gradient_y[i, j] = np.sum(process_region * Gy)

    v_length = np.sqrt(gradient_x**2 + gradient_y**2)

    zero_block = gradient_x.copy()
    zero_block[gradient_x == 0] = 1e-6
    tg = gradient_y / zero_block

    gradient_angle = get_grad_angle(gradient_x, gradient_y, tg)

    suppression = np.zeros_like(v_length, dtype=np.uint8)
    hs, ws = v_length.shape[:2]

    for i in range(1, hs - 1):
        for j in range(1, ws - 1):
            direction = gradient_angle[i, j]
            length = v_length[i, j]

            if direction in [0, 4]:
                neighbours = [v_length[i, j - 1], v_length[i, j + 1]]
            elif direction in [1, 5]:
                neighbours = [v_length[i - 1, j + 1], v_length[i + 1, j - 1]]
            elif direction in [2, 6]:
                neighbours = [v_length[i - 1, j], v_length[i + 1, j]]
            else:
                neighbours = [v_length[i - 1, j - 1], v_length[i + 1, j + 1]]

            if length > max(neighbours):
                suppression[i, j] = 255
            else:
                suppression[i, j] = 0

    max_gradient = np.max(v_length)
    higher_threshold = max_gradient // 6
    lower_threshold = max_gradient // 9

    vivid_border = (v_length >= higher_threshold)
    blur_border = ((v_length >= lower_threshold) & (v_length < higher_threshold))

    final = np.zeros_like(suppression, dtype=np.uint8)
    final[vivid_border & (suppression == 255)] = 255

    for i in range(1, hs - 1):
        for j in range(1, ws - 1):
            if blur_border[i, j] and suppression[i, j] == 255:
                region = final[i-1:i+2, j-1:j+2]
                if np.any(region == 255):
                    final[i, j] = 255

    mask = img.copy()
    mask[final == 255] = [0, 0, 255]

    # cv.imshow("Original", img)
    # cv.imshow("Grayscale|Blurred", img_blurred)
    # cv.imshow("Non-Maximum Suppression", suppression)
    cv.imshow("Double Threshold Result", final)
    cv.imshow("Border", mask)

    cv.waitKey(0)
    cv.destroyAllWindows()

    return v_length, gradient_angle

vl, ga = border_processor("/home/serenity-flaim/Desktop/CV/lab1/media/lab4/sonic_freedom.jpg")
print("Gradient Vector Length Matrix:\n", vl)
print("Gradient Angle Matrix:\n", ga)