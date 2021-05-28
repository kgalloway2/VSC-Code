from PIL import Image
import cv2
from numpy import array
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
import pickle 

X_data = []
for i in range(200):
    img = Image.open("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/screenshots/test_hands/resized_test_hand" + str(i) + ".jpg")
    img_array = array(img)
    X_data.append(img_array.flatten('F'))


Y_data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data)

# this is for normalizing data

scaler = StandardScaler()

# Fit only to the training data
scaler.fit(X_train)

StandardScaler(copy=True, with_mean=True, with_std=True)

# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=(15,15,15),max_iter=1000)

mlp.fit(X_train,Y_train)

predictions = mlp.predict(X_test)


print(confusion_matrix(Y_test,predictions))

print(classification_report(Y_test,predictions))

neural_net = mlp
filehandler = open("C:/Users/kgtrm/Documents/VSC Code/gesture_recognizer/trained_nn.pkl", 'wb') 
pickle.dump(neural_net, filehandler)

# these "print" the weights and biases. however they are too large to be displayed so it is better to put them into a file or something

# for i in range(len(mlp.coefs_)):
#     print("weight matrix between layer ", i, " and layer ", (i+1))
#     print(mlp.coefs_[i])

# for i in range(len(mlp.intercepts_)):
#     print("bias vector at index ", (i+1))
#     print(mlp.intercepts_[i])
