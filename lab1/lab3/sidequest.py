import cv2 as cv
import numpy as np

dim = 5

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

image = cv.imread("/home/serenity-flaim/Desktop/CV/lab1/media/lab3/sonic_wisdom.jpg")
hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
hue, saturation, value = cv.split(hsv_image)

grayscale_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("gray", grayscale_img)

h, w= image.shape[:2]
h = int(h)
w = int(w)
sp_image = grayscale_img.copy()


for i in range(h):
    for j in range(w):
        random_value = np.random.random() 
        if random_value < 0.03:  
            salt_or_pepper = np.random.randint(0, 2)
            if salt_or_pepper == 0:
                sp_image[i, j] = 0   
            else:
                sp_image[i, j] = 255

cv.imshow("Salt Pepper Image", sp_image)

blur_sp_image = sp_image.copy()

kernel5 = form_gauss_kernel(dim, 5)
kernel5 = kernel5 / kernel5.sum()
padding = dim // 2
padded_img = np.pad(grayscale_img, padding, mode='constant', constant_values=0)
blur_sp_image = np.array([[0.0 for _ in range(w)] for _ in range(h)])

for i in range(h):
    for j in range(w):
        process_region = padded_img[i:i+dim, j:j+dim]
        val = np.sum(process_region * kernel5)
        blur_sp_image[i, j] = val

blur_sp_image = np.clip(blur_sp_image, 0, 255).astype(np.uint8)
cv.imshow("Blur SP Image", blur_sp_image)

restored_hsv = cv.merge([hue, saturation, blur_sp_image])
restored_bgr = cv.cvtColor(restored_hsv, cv.COLOR_HSV2BGR)

cv.imshow("Restored Color Image", restored_bgr)

cv.waitKey(0)
cv.destroyAllWindows()