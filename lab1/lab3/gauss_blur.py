import cv2 as cv
import numpy as np

MX_DIMENSION = 5
SQUARE_DEVIATION = 5

def form_gauss_kernel(n, sq_deviation):
    ker = np.array([[0.0 for _ in range(n)] for _ in range(n)])
    a = n - n // 2
    b = a
    for i in range(n):
        for j in range(n):
            x, y = i+1, j+1
            val = (1 / (2 * np.pi * sq_deviation**2)) * np.exp(-(((x-a)**2 + (y-b)**2)/(2 * sq_deviation**2)))
            ker[i][j] = val
    
    return ker



kernel3 = form_gauss_kernel(3, SQUARE_DEVIATION)
kernel5 = form_gauss_kernel(5, SQUARE_DEVIATION)
kernel7 = form_gauss_kernel(7, SQUARE_DEVIATION)

# print("KER 3\n", kernel3)
# print("KER 5\n", kernel5)
# print("KER 7\n", kernel7)


kernel3 = kernel3 / kernel3.sum()
kernel5 = kernel5 / kernel5.sum()
kernel7 = kernel7 / kernel7.sum()

print("Normalized_3 - Sum: ", kernel3.sum(), "\n", kernel3)
print("Normalized_5 - Sum: ", kernel5.sum(), "\n", kernel5)
print("Normalized_7 - Sum: ", kernel7.sum(), "\n", kernel7)

image = cv.imread("/home/serenity-flaim/Desktop/CV/lab1/media/lab3/sonic_wisdom.jpg")
grayscale_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imwrite("/home/serenity-flaim/Desktop/CV/lab1/media/lab3/grayscale.jpg", grayscale_img)

h, w = grayscale_img.shape[:2]
blur_image = np.array([[0.0 for _ in range(w)] for _ in range(h)])

padding = MX_DIMENSION // 2
padded_img = np.pad(grayscale_img, padding, mode='constant', constant_values=0)


for i in range(h):
    for j in range(w):
        process_region = padded_img[i:i+MX_DIMENSION, j:j+MX_DIMENSION]
        val = np.sum(process_region * kernel5)
        blur_image[i, j] = val

blur_image = np.clip(blur_image, 0, 255).astype(np.uint8)
cv.imwrite("/home/serenity-flaim/Desktop/CV/lab1/media/lab3/gaussian_blur.jpg", blur_image)