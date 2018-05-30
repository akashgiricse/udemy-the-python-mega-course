import cv2
# import time

video = cv2.VideoCapture(0)  # 0 is used for webcam

# to check how many frames has been generated
a = 0
while True:
    a = a + 1
    check, frame = video.read()
    # check is a boolean to check whether camera is open or not
    # frame is a numpy array for capturing video
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # stop the script for 3 seconds
    # time.sleep(3)

    cv2.imshow("Capturing", gray)
    key = cv2.waitKey(1)  # 1 micro second
    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()
