import cv2 as cv
import numpy as np

def form_gauss_kernel(n, sq_deviation):
    ker = [[0.0 for _ in range(n)] for _ in range(n)]
    a = n - n // 2
    b = a
    for i in range(n):
        for j in range(n):
            x, y = i+1, j+1
            val = (1 / (2 * np.pi * sq_deviation**2)) * np.exp(-(((x-a)**2 + (y-b)**2)/(2 * sq_deviation**2)))
            ker[i][j] = val
    
    return ker

ker = form_gauss_kernel(3, 5)
print(ker)