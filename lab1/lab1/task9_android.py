import cv2 as cv

def display_phone_camera():
    url = "http://10.205.66.144:8080/video"
    cap = cv.VideoCapture(url)
    
    while True:
        ok, fr = cap.read()
        if not ok:
            break
        cv.imshow("Phone Camera!", fr)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv.destroyAllWindows()

display_phone_camera()