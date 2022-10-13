# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:28:59 2022

@author: zethi
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('CarPricePrediction_Model.sav','rb'))

# Function for predciton

def price_prediction(input_data):
    
    
     
    input_data_nparr = np.asarray(input_data,dtype=object)

    input_data_reshaped = input_data_nparr.reshape(1,-1)
    
    data = input_data_reshaped

    

    Price_prediction = loaded_model.predict(data)

    return Price_prediction[0]



def main():
    
    #title
    st.title("Your Car Your Money")
    
    # Getting input from user
#    Year	Kilometers_Driven	Owner_Type	Seats	Diesel	Petrol	Automatic	Manual	Mileage-km/li	Power-bhp	Engine-CC
    
    Year                        = st.text_input("Year Car Purchased")
    Kilometers_Driven           = st.text_input("Kilometers Car Drived") 
    Owner_Type                  = st.text_input("Car OwnerShip (1,2,3,4)") 
    Seats                       = st.text_input("Seats Count") 
    Diesel                      = st.text_input("Diesel Engine (yes-1,no-0)") 
    Petrol                      = st.text_input("Petrol Engine (yes-1,no-0)") 
    Automatic                   = st.text_input("Automatic Gearing (yes-1,no-0)") 
    Manual                      = st.text_input("Manual Gearing (yes-1,no-0)") 
    Mileage                     = st.text_input("Mileage-km/li") 
    Power                       = st.text_input("Power-bhp") 
    Engine                      = st.text_input("Engine-CC") 
    
    #code for predicction
    cost = 0
    
    
    #Creating button for prediction
    if st.button("Make Cost"):
        cost = price_prediction([Year, Kilometers_Driven, Owner_Type, Seats, Diesel, Petrol, Automatic, Manual, Mileage, Power, Engine])
    
    
    
    st.success(cost)
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
