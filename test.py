import pickle
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
import numpy as np

stand= StandardScaler()
# input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)
input_data = (1,63,3,145,233,1,0,150,0,2.3,0,0,1)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)
# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

test=pickle.load(open("D:/final_yeara_project/FinalYearProject/BE/mlModels/heart_model.sav","rb"))

prediction = test.predict(input_data_reshaped)
print(prediction)
