from PIL import Image
# 640x480

i = 0
while i <= 103:
    img=Image.open("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/test_hands/test_hand" + str(i) + ".jpg")

    c_i = img.crop(box=(20,20,550,400))

    c_i.save("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/test_hands/cropped_test_hand" + str(i) + ".jpg")

    i += 1

