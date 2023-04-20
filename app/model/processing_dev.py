import pandas as pd
import lightgbm as lgb
import numpy as np
import re
import csv
import pickle
import sys
import os
import sqlite3

def load_model():
    with open('/app/model/model_0.pickle', mode='rb') as f:
        model_0 = pickle.load(f)
    with open('/app/model/model_1.pickle', mode='rb') as f:
        model_1 = pickle.load(f)
    return model_0,model_1

def make_title_df(df):

    return meisi_df

def pre_processing(df):

    return x_test

def update_web(value, pk):
    print(value, pk)
    try:
        with sqlite3.connect("/app/db.sqlite3") as con:
            cur = con.cursor()
            a = cur.execute(f"UPDATE predict_app_post SET result_path = '{value}' WHERE id={pk};")
            con.commit()
    except Exception as e:
        print("sql",e)

columns = []

if __name__ == '__main__':
    args = sys.argv
    dir_path = args[1]
    pk = args[2]
    data_path = os.path.join(dir_path,"data.csv")
    df = pd.read_csv(data_path, index_col=0)
    df_fillna = df[columns].copy()

    x_test = pre_processing(df_fillna)

    model1,model2 = load_model()
 
    model1_pred = model1.predict(
        x_test, 
        num_iteration=model1.best_iteration
        )

    model2_pred = model2.predict(
        x_test, 
        num_iteration=model2.best_iteration
        )

    pred_df = pd.DataFrame(
        {
            "model1_pred":model1_pred,
            "model2_pred":model2_pred
            })
    # np.corrcoef(df["p_ave_household"].values,p_ave_household_pred)
    data_path = os.path.join(dir_path,"result.csv")
    pred_df.to_csv(data_path, index=False)
    update_web(data_path, pk)
