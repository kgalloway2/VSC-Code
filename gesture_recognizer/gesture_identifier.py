import cv2
import time
from PIL import Image
from numpy import array
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
import pickle

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

currentframe = 0
while rval and currentframe < 50:
    time.sleep(0.2)
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    if rval:
        # if video is still left continue creating images
        name = 'C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/testing/hand' + str(currentframe) + '.jpg'
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

for i in range(50):
    # print("Reformatting image ", i)
    # open image
    img=Image.open("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/testing/hand" + str(i) + ".jpg")

    # crop image
    cropped_img = img.crop(box=(100,100,500,400))

    #scale down to more pixelated version
    imgSmall = cropped_img.resize((40,30),resample=Image.BILINEAR)

    # Scale back up using NEAREST to original size
    result = imgSmall.resize(img.size,Image.NEAREST)

    # Save
    result.save("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/testing/resized_hand" + str(i) + ".jpg")

hand_data = []
for i in range(50):
    img = Image.open("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/testing/resized_hand" + str(i) + ".jpg")
    img_array = array(img)
    hand_data.append(img_array.flatten('F'))

filehandler = open("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/trained_nn.pkl", 'rb') 
mlp = pickle.load(filehandler)

results = mlp.predict(hand_data)
print(results)