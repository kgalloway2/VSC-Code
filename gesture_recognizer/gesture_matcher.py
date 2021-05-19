from numpy import array
from numpy import linalg
from PIL import Image
import cv2

predicted = []
for k in range(0,106):
    print("checking image: ", k)
    im_1 = Image.open("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/test_hands/cropped_test_hand"+ str(k) +".jpg")
    ar1 = array(im_1)

    histogram1 = cv2.calcHist([ar1], [0], None, [256], [0, 256])

    closed_closest_pic = 0
    closed_current_min = float('inf')
    for i in range(1,167):
        im_2 = Image.open("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/closed_hand/cropped_closed_hand" + str(i) + ".jpg")
        ar2 = array(im_2)
        histogram2 = cv2.calcHist([ar2], [0], None, [256], [0, 256])
        current_diff = 0
        j = 0
        while j<len(histogram1) and j<len(histogram2):
            current_diff+=(histogram1[j]-histogram2[j])**2
            j+= 1
        current_diff = current_diff**(1 / 2)
        if current_diff < closed_current_min:
            closed_closest_pic = i
            closed_current_min = current_diff

    open_closest_pic = 0
    open_current_min = float('inf')
    for i in range(1,161):
        im_2 = Image.open("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/open_hand/cropped_open_hand" + str(i) + ".jpg")
        ar2 = array(im_2)
        histogram2 = cv2.calcHist([ar2], [0], None, [256], [0, 256])
        current_diff = 0
        j = 0
        while j<len(histogram1) and j<len(histogram2):
            current_diff+=(histogram1[j]-histogram2[j])**2
            j+= 1
        current_diff = current_diff**(1 / 2)
        if current_diff < open_current_min:
            open_closest_pic = i
            open_current_min = current_diff
    print(open_current_min, " ", closed_current_min)
    if open_current_min < closed_current_min:
        # print(open_closest_pic)
        # print(open_current_min)
        # open_hand = True
        # closest = Image.open("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/open_hand/cropped_open_hand" + str(open_closest_pic) + ".jpg")
        # closest.show()
        predicted.append(1)
    else:
        # print(closed_closest_pic)
        # print(closed_current_min)
        # open_hand = False
        # closest = Image.open("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/closed_hand/cropped_closed_hand" + str(closed_closest_pic) + ".jpg")
        # closest.show()
        predicted.append(0)

actual = [1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,
1,1,1,1,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0]

num_corrects = 0
for h in range(len(actual)):
    if actual[h] == predicted[h]:
        num_corrects += 1
    else:
        pass

print(predicted)
print(num_corrects)
print(num_corrects / len(predicted))