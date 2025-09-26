import cv2 as cv
def write_video_to_file(origin_path, output_path):
    cap = cv.VideoCapture(origin_path)
    w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    vid_writer = cv.VideoWriter(output_path, fourcc, 33, (w, h))
    while True:
        ok, img = cap.read()
        if not ok:
            break
        cv.imshow("img", img)
        vid_writer.write(img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

write_video_to_file("/home/serenity-flaim/Desktop/CV/lab1/media/не-обязан.mp4", "/home/serenity-flaim/Desktop/CV/lab1/media/output.mp4")
