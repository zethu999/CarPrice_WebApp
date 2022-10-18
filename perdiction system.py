# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

loaded_model = pickle.load(open('D:/Programs/DataScience_env/Car_Price _predection/CarPricePrediction_Model.sav','rb'))

input_data = [2012,87000,1,7,1,0,0,1,20.77,88.76,1248]
 
input_data_nparr = np.asarray(input_data)

input_data_reshaped = input_data_nparr.reshape(1,-1)

print(input_data_reshaped)

Price_prediction = loaded_model.predict(input_data_reshaped)

print(Price_prediction[0])
print(type(Price_prediction[0]))