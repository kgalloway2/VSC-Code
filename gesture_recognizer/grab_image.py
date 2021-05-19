# this script uses the webcam to take screenshots and write them to files in a folder

import cv2
import time

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

currentframe = 0
while rval:
    time.sleep(0.2)
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    if rval:
        # if video is still left continue creating images
        name = 'C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/test_hands/test_hand' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        #make the image grayscale to process more easily
        gray_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # writing the extracted images
        cv2.imwrite(name, gray_image)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break
cv2.destroyWindow("preview")