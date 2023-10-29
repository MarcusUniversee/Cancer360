
# """Base state for the app."""

import reflex as rx
import re
import pickle
# from Cancer360.state import State
import numpy as np
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout , BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau
import os

def getModelArchitecture():
    model = Sequential()
    model.add(Conv2D(32 , (3,3) , strides = 1 , padding = 'same' , activation = 'relu' , input_shape = (512,512,3)))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2) , strides = 2 , padding = 'same'))
    model.add(Conv2D(64 , (3,3) , strides = 1 , padding = 'same' , activation = 'relu'))
    model.add(Dropout(0.1))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2) , strides = 2 , padding = 'same'))
    model.add(Conv2D(64 , (3,3) , strides = 1 , padding = 'same' , activation = 'relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2) , strides = 2 , padding = 'same'))
    model.add(Conv2D(128 , (3,3) , strides = 1 , padding = 'same' , activation = 'relu'))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2) , strides = 2 , padding = 'same'))
    model.add(Conv2D(256 , (3,3) , strides = 1 , padding = 'same' , activation = 'relu'))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2) , strides = 2 , padding = 'same'))
    model.add(Flatten())
    model.add(Dense(units = 128 , activation = 'relu'))
    model.add(Dropout(0.2))
    model.add(Dense(units = 1 , activation = 'sigmoid'))
    model.compile(optimizer = "rmsprop" , loss = 'binary_crossentropy' , metrics = ['accuracy'])
    model.summary()
    return model


img = plt.imread('./test_image.jpg')
img = np.array(img)  

test_model = getModelArchitecture()  # assuming you have a function to create your model architecture
test_model.load_weights('./cnn_weights.h5')
test_prediction = test_model.predict(np.array([img]))
# class TimmyAppointmentFormState(State):
#     form_data: dict = {}
#     data_filled: bool = False
#     results: float
#     def handle_submit_data(self, form_data: dict):
#         self.form_data = form_data
#         self.data_filled = True
#         self.results = text_analysis(form_data)
        
#     def handle_clear_data(self):
#         self.form_data.clear()
#         self.data_filled = False

# # pip freeze > requirements.txt
# class CNNState(State):
#     """The app state."""

#     # The images to show.
#     img: list[str]
#     prediction_accuracy: float

#     async def handle_upload(
#         self, files: list[rx.UploadFile]
#     ):
#         """Handle the upload of file(s).

#         Args:
#             files: The uploaded files.
#         """
#         for file in files:
#             upload_data = await file.read()
#             outfile = rx.get_asset_path(file.filename)

#             with open(outfile, "wb") as file_object:
#                 file_object.write(upload_data)

#             self.img.append(file.filename)
            
#         self.prediction_accuracy = self.CNNPred(self.img[0])
           
            
#     def CNNPred(image_input, path = './cnn_weights.h5'):
#         model = getModelArchitecture()  # assuming you have a function to create your model architecture
#         model.load_weights(path)
        
#         test_prediction = model.predict(np.array([image_input]))
#         print(test_prediction)
#         return test_prediction[0][0]

# def text_analysis(data = TimmyAppointmentFormState.form_data):
#     res = []
#     age = int(data["Age"])
#     res.append(age)
    
#     gender = data["Gender"]
#     main_data = data["Input"] or 'hi :)'
    
#     if(gender.lower() == "male"):
#         res.append(1)
#         res.append(0)
#     else:
#         res.append(0)
#         res.append(1)
        
#     relevant_queries = ['ALCOHOL','CHEST PAIN','SHORTNESS OF BREATH','COUGHING','PEER PRESSURE','CHRONIC DISEASE','SWALLOWING DIFFICULTY', 'YELLOW FINGERS', 'ANXIETY', 'FATIGUE', 'ALLERGY', 'WHEEZING']
    
#     for i in relevant_queries:
#         I = i.lower()
#         if(I in main_data.lower()):
#             res.append(1)
#         else:
#             res.append(0)

#     return getPred(np.array(res), './xgb_model.pkl')
    
# def getPred(x_inputs, path):
#     with open(path, "rb") as file:
#         loaded_xgb = pickle.load(file)
        
#     # test = [61, False, True, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2]
#     xgb_pred = loaded_xgb.predict_proba([x_inputs])

#     return float(xgb_pred[0][1] * 100)


# def getModelArchitecture():
#         model = Sequential()
#         model.add(Conv2D(32 , (3,3) , strides = 1 , padding = 'same' , activation = 'relu' , input_shape = (512,512,3)))
#         model.add(BatchNormalization())
#         model.add(MaxPool2D((2,2) , strides = 2 , padding = 'same'))
#         model.add(Conv2D(64 , (3,3) , strides = 1 , padding = 'same' , activation = 'relu'))
#         model.add(Dropout(0.1))
#         model.add(BatchNormalization())
#         model.add(MaxPool2D((2,2) , strides = 2 , padding = 'same'))
#         model.add(Conv2D(64 , (3,3) , strides = 1 , padding = 'same' , activation = 'relu'))
#         model.add(BatchNormalization())
#         model.add(MaxPool2D((2,2) , strides = 2 , padding = 'same'))
#         model.add(Conv2D(128 , (3,3) , strides = 1 , padding = 'same' , activation = 'relu'))
#         model.add(Dropout(0.2))
#         model.add(BatchNormalization())
#         model.add(MaxPool2D((2,2) , strides = 2 , padding = 'same'))
#         model.add(Conv2D(256 , (3,3) , strides = 1 , padding = 'same' , activation = 'relu'))
#         model.add(Dropout(0.2))
#         model.add(BatchNormalization())
#         model.add(MaxPool2D((2,2) , strides = 2 , padding = 'same'))
#         model.add(Flatten())
#         model.add(Dense(units = 128 , activation = 'relu'))
#         model.add(Dropout(0.2))
#         model.add(Dense(units = 1 , activation = 'sigmoid'))
#         model.compile(optimizer = "rmsprop" , loss = 'binary_crossentropy' , metrics = ['accuracy'])
#         model.summary()
#         return model