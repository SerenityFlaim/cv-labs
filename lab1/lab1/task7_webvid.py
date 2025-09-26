import cv2 as cv
def record_video():
    cap = cv.VideoCapture(0)
    w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv.CAP_PROP_FPS)
    print(fps)
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    video_writer = cv.VideoWriter("media/webcamOutput.mp4", fourcc, fps, (w, h))
    while (True):
        ok, img = cap.read()
        if not ok:
            break
        video_writer.write(img)
        cv.imshow("Recording", img)
        if cv.waitKey(33) & 0xFF == ord('q'):
            break
    cap.release()
    video_writer.release()
    cv.destroyAllWindows()

record_video()