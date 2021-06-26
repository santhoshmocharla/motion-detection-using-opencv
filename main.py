import cv2
import winsound
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frameone = cam.read()
    ret, frametwo = cam.read()
    differnce = cv2.absdiff(frameone,frametwo)
    grey = cv2.cvtColor(differnce, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(grey ,(5, 5), 0)
    _, thr = cv2.threshold(blur, 20, 200, cv2.THRESH_BINARY)
    dilate = cv2.dilate(thr, None, iterations=3)
    contour, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in contour:
        if cv2.contourArea(c) < 3000:
            continue
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frameone,(x, y), (x+w, y+h), (0,255,0), 2)
        winsound.PlaySound('beep.wav', winsound.SND_ASYNC)
    if cv2.waitKey(10) == ord('x'):
        break
    cv2.imshow('SANTHOSH CAM', frameone)