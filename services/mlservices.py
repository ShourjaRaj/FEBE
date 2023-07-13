from starlette.responses import JSONResponse
import numpy as np
from utility.messages import (
    getSuccessMessage,
    getErrorMessage
)

from mlModels.read import read_diabetes,read_heart

def diabetes(data):
    try:
        inp_data=(data.gender,data.age,data.hypertension,data.heart_disease,data.smoking,data.bmi,data.HbA1c_level,data.blood_glucose_level)
        inp_data_as_numpy_array= np.asarray(inp_data)
        # reshape the numpy array as we are predicting for only on instance
        inp_data_reshaped = inp_data_as_numpy_array.reshape(1,-1)
        model=read_diabetes()
        res=model.predict(inp_data_reshaped)
        print(res)
        if(res[0]==0):
            return JSONResponse(getSuccessMessage(False))
        return JSONResponse(getSuccessMessage(True))
    except Exception as e:
        print(str(e))
        return JSONResponse(getErrorMessage(str(e)),status_code=500)
    
    
    
def heart(data):
    try:
        print("123",data)
        inp_data=(data.age,data.gender,data.cp,data.trestbps,data.chol,data.fbs,data.restecg,data.thalach,data.exang,data.oldpeak,data.slope,data.ca,data.thal)
        inp_data_as_numpy_array= np.asarray(inp_data)
        # reshape the numpy array as we are predicting for only on instance
        inp_data_reshaped = inp_data_as_numpy_array.reshape(1,-1)
        model=read_heart()
        res=model.predict(inp_data_reshaped)
        print(res)
        if(res[0]==0):
            return JSONResponse(getSuccessMessage(False))
        return JSONResponse(getSuccessMessage(True))
    except Exception as e:
        print(str(e))
        return JSONResponse(getErrorMessage(str(e)),status_code=500)
    
     