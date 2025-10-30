import os
import sys
import dill

import numpy as np
import pandas as pd


from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging  

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

   
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    


def evaluate_models(x_train,y_train,x_test,y_test,models):
    try:
        report={}

        for i in range(len(list(models))):
            model=list(models.values())[i]
            # Train model
            model.fit(x_train,y_train)

            # Predicting the test set
            y_test_pred=model.predict(x_test)

            #Predicting train set
            y_train_pred=model.predict(x_train)
            
            # R2 Score
            test_model_score=r2_score(y_test,y_test_pred)
            train_model_score=r2_score(y_train,y_train_pred)

            report[list(models.keys())[i]]={"test_score":test_model_score,"train_score":train_model_score}

        return report

    except Exception as e:
        raise CustomException(e,sys)