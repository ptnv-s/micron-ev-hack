from flask import Flask, render_template
import numpy as np
import folium
import pickle
import math
import osmnx
import utm
import pandas as pd

app = Flask(__name__)

# m = folium.Map(location=[20.5937, 78.9629],width=500, height=500, zoom_start=5)
# m.save('map.html')
#model=pickle.load(open('optimal_pred_model2.pkl','rb'))


@app.route('/',methods = ['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/predict',methods = ['GET', 'POST'])
def predict():
     return render_template('res.html')


if  __name__ == '__main__':
    app.run(debug=True)
