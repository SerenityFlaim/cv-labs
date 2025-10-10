import cv2 as cv
import numpy as np

lower1 = np.array([0, 120, 70])
upper1 = np.array([10, 255, 255])
lower2 = np.array([170, 120, 70])
upper2 = np.array([179, 255, 255])

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))

cap = cv.VideoCapture(0)
while True:
    ok, img = cap.read()
    if not ok:
        break
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    mask1 = cv.inRange(hsv_img, lower1, upper1)
    mask2 = cv.inRange(hsv_img, lower2, upper2)
    mask = cv.bitwise_or(mask1, mask2)

    bw_filter = cv.dilate(cv.erode(mask, kernel, iterations=1), kernel, iterations=1)
    bw_filter = cv.erode(cv.dilate(bw_filter, kernel, iterations=1), kernel, iterations=1)


    M = cv.moments(bw_filter)
    area = M['m00']
    print(area)
    final_img = img
    if area:
        # max_countour = max(contours, key=cv.contourArea)
        # area = cv.contourArea(max_countour)
        # x, y, w, h = cv.boundingRect(max_countour)
        # M = cv.moments(max_countour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv.circle(final_img, (cx, cy), 6, (0,255,0), -1)

        #cv.rectangle(final_img, (x, y), (x + w, y + h), (0, 0, 0), 2)
        cv.putText(final_img, f"Area: {int(area)}", (10,30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
        cv.putText(final_img, f"Centroid: ({cx},{cy})", (10,60), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
    else:
        cv.putText(final_img, "No object", (10,30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

    cv.imshow('Find Red', final_img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()