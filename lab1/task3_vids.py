import cv2 as cv
def display_video(path, name, size="", color=""):
    cap = cv.VideoCapture(path)
    cv.namedWindow(name, cv.WINDOW_NORMAL)

    match size:
        case "small":
            cv.resizeWindow(name, 700, 400)
        case "medium":
            cv.resizeWindow(name, 1080, 512)
        case "big":
            cv.resizeWindow(name, 1540, 1080)

    while True:
        ret, frame = cap.read()
        if not (ret):
            break
        match color:
            case "invert":
                frame = cv.bitwise_not(frame)
            case "gray":
                frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            case "rainbow":
                frame = cv.applyColorMap(frame, cv.COLORMAP_RAINBOW)
            case "pink":
                frame = cv.applyColorMap(frame, cv.COLORMAP_PINK)
        cv.imshow(name, frame)
        if cv.waitKey(33) & 0xFF == 27:
            break
    
    cap.set(cv.CAP_PROP_POS_FRAMES, 0)
    cv.destroyWindow(name)
    cap.release()

display_video("/home/serenity-flaim/Desktop/CV/lab1/media/не-обязан.mp4", "Origin")
display_video("/home/serenity-flaim/Desktop/CV/lab1/media/не-обязан.mp4", "small", size="small")
display_video("/home/serenity-flaim/Desktop/CV/lab1/media/не-обязан.mp4", "Medium Gray", size="medium", color="gray")
display_video("/home/serenity-flaim/Desktop/CV/lab1/media/не-обязан.mp4", "Big Rainbow", size="big", color="rainbow")
display_video("/home/serenity-flaim/Desktop/CV/lab1/media/не-обязан.mp4", "Inverted Origin", size="big", color="invert")
display_video("/home/serenity-flaim/Desktop/CV/lab1/media/не-обязан.mp4", "BIG PINK", size="big", color="pink")