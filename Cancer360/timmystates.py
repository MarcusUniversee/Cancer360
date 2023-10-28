"""Base state for the app."""

import reflex as rx
import re
import pickle
from Cancer360.state import State
import numpy as np
from xgboost import XGBClassifier

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

def text_analysis(data = TimmyAppointmentFormState.form_data):
    res = []
    age = int(data["Age"])
    res.append(age)
    
    gender = data["Gender"]
    main_data = data["Input"] or 'hi :)'
    
    if(gender.lower() == "male"):
        res.append(1)
        res.append(0)
    else:
        res.append(0)
        res.append(1)
        
    relevant_queries = ['ALCOHOL','CHEST PAIN','SHORTNESS OF BREATH','COUGHING','PEER PRESSURE','CHRONIC DISEASE','SWALLOWING DIFFICULTY', 'YELLOW FINGERS', 'ANXIETY', 'FATIGUE', 'ALLERGY', 'WHEEZING']
    
    for i in relevant_queries:
        I = i.lower()
        if(I in main_data.lower()):
            res.append(1)
        else:
            res.append(0)

    return getPred(np.array(res))
    
def getPred(x_inputs, path = '../../xgb_model.pkl'):
    with open("xgb_model.pkl", "rb") as file:
        loaded_xgb = pickle.load(file)
        
    # test = [61, False, True, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2]
    xgb_pred = loaded_xgb.predict_proba([x_inputs])

    return float(xgb_pred[0][1] * 100)