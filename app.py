# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 15:44:47 2023

@author: Dell
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request
import pickle

from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model1.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        sepal_length = float(request.form['sepal length'])
        sepal_width = float(request.form['sepal width'])
        petal_length = float(request.form['petal length'])
        petal_width = float(request.form['petal width'])
   
        prediction=model.predict([[sepal_length,sepal_width,petal_length,petal_width ]])
        
        
        return render_template('index.html',prediction_text=prediction)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)


