import cv2 as cv
import numpy as np

MX_DIMENSION = 5
SQUARE_DEVIATION = 1

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

print("KER 3\n", kernel3, "\n")
print(kernel3.sum())
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
#cv.imwrite("/home/serenity-flaim/Desktop/CV/lab1/media/lab3/grayscale.jpg", grayscale_img)

h, w = grayscale_img.shape[:2]
dims = [3, 7]
deviations = [3, 30]

for dim in dims:
    for dvn in deviations:
        cur_ker = form_gauss_kernel(dim, dvn)
        cur_ker = cur_ker / cur_ker.sum()

        padding = dim // 2
        padded_img = np.pad(grayscale_img, padding, mode='constant', constant_values=0)
        blur_image = np.array([[0.0 for _ in range(w)] for _ in range(h)])

        for i in range(h):
            for j in range(w):
                process_region = padded_img[i:i+dim, j:j+dim]
                val = np.sum(process_region * cur_ker)
                blur_image[i, j] = val

        blur_image = np.clip(blur_image, 0, 255).astype(np.uint8)
        filename = f"gaussian_blur_dim{dim}_dvn{dvn}"
        cv.imwrite(f"/home/serenity-flaim/Desktop/CV/lab1/media/lab3/{filename}.jpg", blur_image)

        cv_blur = cv.GaussianBlur(grayscale_img, (dim, dim), dvn)
        cv_filename = f"CV_blur_dim{dim}_dvn{dvn}"
        cv.imwrite(f"/home/serenity-flaim/Desktop/CV/lab1/media/lab3/{cv_filename}.jpg", cv_blur)