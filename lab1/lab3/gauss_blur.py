import cv2 as cv
import numpy as np

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