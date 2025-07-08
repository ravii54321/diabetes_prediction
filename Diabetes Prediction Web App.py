#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 14:25:57 2025

@author: rabisankardas
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('/Users/rabisankardas/Downloads/trained_model.sav', 'rb'))


# creating a function for prediction

def diabetes_prediction(input):
    

    # changing the inpt_data to numpy array
    # np.asaaray converts the list to an atrray

    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the data as i am predicting for one instace
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction =loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return'The person is not diabetic' 
    else:
      return'The person is diabetic'
      
      
      
    def main():
       
       
      # giving a title
      st.title('Diabetes Prediction Web App')
      
      
      # getting the input data from the user
      
      
      Pregnancies = st.text_input('Number Of Pragnancies')
      Glucose = st.text_input('Glucose Level')
      BloodPressure = st.text_input('Blood Pressure Value')
      SkinThickness = st.text_input('Skin Thickness Value')
      Insulin = st.text_input('Insulin level')
      BMI = st.text_input('BMI Value')
      DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Value')
      Age = st.text_input('Age Of The Person')
      
      
      #code for prediction
      diagnosis = ''
      
      # creating a button for prediction
      if st.button('Diabetes Test Result'):
         diagnosis = diabetes_prediction([Pregnancies, Glucose,  BloodPressure, SkinThickness,  Insulin,  BMI,  DiabetesPedigreeFunction, Age])
         
         
         st.success(diagnosis)
         
         
         
         
         if __name__ == '__main__':
             main()
         
         
         
         
         
       
     
     
     
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      