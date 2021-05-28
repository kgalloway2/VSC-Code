from PIL import Image

# 640x480

i = 0
while i <= 199:
    # print("Reformatting image ", i)
    # open image
    img=Image.open("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/test_hands/test_hand" + str(i) + ".jpg")

    # crop image
    cropped_img = img.crop(box=(100,100,500,400))

    #scale down to more pixelated version
    imgSmall = cropped_img.resize((40,30),resample=Image.BILINEAR)

    # Scale back up using NEAREST to original size
    result = imgSmall.resize(img.size,Image.NEAREST)

    # Save
    result.save("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/test_hands/resized_test_hand" + str(i) + ".jpg")
    
    i += 1

print("Done resizing images.")