from flask import Flask,request
import pandas as pd
import numpy as np
import pickle


app=Flask(__name__)
pickle_in=open("C:/Users/datas/Untitled Folder/classifier.pkl","rb")
classifier=pickle.load(pickle_in)


@app.route("/")
def welcome():
    return "Welcome All"

@app.route("/predict")
def pred_auth():
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted values is "+str(prediction)


@app.route('/predict_file', methods =['GET', 'POST' ])
def pred_note():
    df_test=pd.read_csv(request.files.get("file"))
    prediction=classifier.predict(df_test)
    return "The predicted values for the csv is "+str(list(prediction))

if __name__=='__main__':
    app.run()