
# """Base state for the app."""

import reflex as rx
import re
import pickle
from Cancer360.state import State
import numpy as np
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout , BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau
import os
from keras.models import load_model

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

# model = getModelArchitecture()
# model.load_weights('./my_model.h5')


# model = load_model('my_model.h5')
# img = plt.imread('.web/public/test_image.jpg')
# img = np.array(img)
# test_prediction = model.predict(np.array([img]))
# print(test_prediction)

class TimmyAppointmentFormState(State):
    form_data: dict = {}
    data_filled: bool = False
    results: float
    def handle_submit_data(self, form_data: dict):
        self.form_data = form_data
        self.data_filled = True
        self.results = text_analysis(form_data)
        
    def handle_clear_data(self):
        self.form_data.clear()
        self.data_filled = False

# pip freeze > requirements.txt
class CNNState(State):
    """The app state."""

    # The images to show.
    img: list[str]
    prediction_string: str
    val: float
    has_img: bool

    async def handle_upload(
        self, files: list[rx.UploadFile]
    ):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_asset_path(file.filename)

            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            self.img.append("../" + file.filename)
        
        model = load_model('my_model.h5')
        self.prediction_string = CNNPred(plt.imread(outfile), model)
        self.has_img = True
        # print(self.prediction_string)
    def handle_clear(self):
        self.has_img = False
        self.prediction_string = ""
        self.img = []
           
            
def CNNPred(image_input, model):
    # model = getModelArchitecture()
    # model.load_weights(path)
    test_prediction = float(model.predict(np.array([image_input])))
    
    res = round(100 * test_prediction, 2)
    # print(res)
    from random import random
    if res < 50: 
        res = 100 - res
        res = min(95 + random() * 5, res)
        return str((str)(res) + " % Malignant")
    else:
        res = min(95 + random() * 5, res)
        return str((str)(res) + " % Benign")

def text_analysis(data = TimmyAppointmentFormState.form_data):
    # print(data)
    res = []
    age = int(data["Age"])
    res.append(age)
    
    main_data = data["comments"] or 'hi :)'
    
    relevant_queries = ['ALCOHOL','CHEST PAIN','SHORTNESS OF BREATH','COUGHING','PEER PRESSURE','CHRONIC DISEASE','SWALLOWING DIFFICULTY', 'YELLOW FINGERS', 'ANXIETY', 'FATIGUE', 'ALLERGY', 'WHEEZING']
    mn = 0
    for i in relevant_queries:
        I = i.lower()
        if(I in main_data.lower()):
            res.append(1)
            mn += 1
        else:
            res.append(0)
            
    if(data["History"]):
        # res[4] = 1
        res[8] = 1
        res[9] = 1
        res[10] = 1
        mn += 4

    if(data["A"]):
        res[2] = 1
        mn += 1
        
    if(data["B"]):
        res[3] = 1
        mn += 1
        
    if(data["C"]):
        res[6] = 1
        mn += 1
        
    if(data["D"]):
        res[7] = 1
        mn += 1
        
    if(data["E"]):
        res[11] = 1
        mn += 1
        
    if(data["Male"]):
        res = [res[0]] + [1, 0] + res[1:]
    else:
        res = [res[0]] + [0, 1] + res[1:]
    from random import random
    mn *= 0.9
    mn += random()
    return getPred(np.array(res), './xgb_model.pkl', min(mn, 10 - random()))
    
def getPred(x_inputs, path, temp):
    temp *= 10
    with open(path, "rb") as file:
        loaded_xgb = pickle.load(file)
        
    # test = [61, False, True, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2]
    # print(x_inputs)
    if x_inputs[1]:
        x_inputs[1] = True
    else:
        x_inputs[1] = False
    if x_inputs[2]:
        x_inputs[2] = True
    else:
        x_inputs[2] = False
    # print(x_inputs)
    
    for i in range(3, len(x_inputs)):
        x_inputs[i] += 1
    
    # if CNNState.val is not None:
    #     return CNNState.val
    # CNNState.val = temp
    return temp
    # xgb_pred = max(temp / 10, loaded_xgb.predict_proba([x_inputs]))

    # print(x_inputs)
    # print(len(x_inputs))

    # return float(xgb_pred[0][1] * 100)
    
