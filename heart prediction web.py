#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:20:31 2024

@author: payalteyung
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('/Users/payalteyung/Desktop/DA/trained_model.sav','rb'))

#creating a function for prediction


def heartDisease_prediction(input_data):
    

    #changing the input data to a numpy array

    numpy_array = np.asarray(input_data)

    #reshape the numpy array as we predicting for only one instance
    reshaped = numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(reshaped)
    print(prediction)

    if(prediction[0]==0):
        return 'The person doesnot have heart disease'
    else:
        return 'The person has heart disease'
    
    
def main():
    
    st.title('Heart Disease Prediction')
    
    
    
    age = st.number_input('Age')
    sex = st.number_input('Gender')
    cp = st.number_input('Chest Pain Type')
    trestbps = st.number_input('Resting Blood Pressure')
    chol = st.number_input('Cholestrol')
    fbs = st.number_input('Fasting Blood Sugar')
    restecg = st.number_input('Resting ecg')
    thalach = st.number_input('Maximum Heart Rate')
    exang = st.number_input(' Exercise Induced Angina')
    oldpeak = st.number_input(' ST depression induced by exercise relative to rest')
    slope = st.number_input(' Slope of Peak Exercise ST segment')
    ca = st.number_input(' Number of Major Vessels')
    thal = st.number_input('Hemoglobin')
    
    
    diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        diagnosis = heartDisease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
        
    st.success(diagnosis)
    
    
if __name__=='__main__':
    main()
    
    
    
    