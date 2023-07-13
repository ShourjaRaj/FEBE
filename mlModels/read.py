import pickle

def read_diabetes():
    return pickle.load(open('D:/final_yeara_project/FinalYearProject/BE/mlModels/new_diabetes_model.sav','rb'))


def read_heart():
    return pickle.load(open('D:/final_yeara_project/FinalYearProject/BE/mlModels/heart_model.sav','rb'))
