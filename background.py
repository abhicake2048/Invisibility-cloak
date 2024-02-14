import cv2
import os


filename = "backer.jpg"
if os.path.exists(filename):
    os.remove(filename)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, background = cap.read()
    if ret:
        cv2.imshow("image",background)
        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite(filename,background)
            break

cap.release()
cv2.destroyAllWindows()