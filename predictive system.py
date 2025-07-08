# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle 

#loading the saved model
loaded_model = pickle.load(open('/Users/rabisankardas/Downloads/trained_model.sav', 'rb'))

input_data = (1,189,60,23,846,30.1,0.398,59)

# changing the inpt_data to numpy array
# np.asaaray converts the list to an atrray

input_data_as_numpy_array = np.asarray(input_data)

#reshape the data as i am predicting for one instace
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction =loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')