from flask import Flask,request, render_template
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
def predict_optimal_place(lat,lon):
  new_model = pickle.load(open("optimal_pred_model3.pkl", "rb"))

  # converting lat, lon from WGS4 to UT,
  easting, northing, _, _ = utm.from_latlon(lat, lon)

  # adding 250 metres buffer to the user input coordinates to give surrounding amenity data
  easting = easting + 250
  northing = northing + 250

  # converting back to lat, lon

  lat1, lon1 = utm.to_latlon(easting, northing, 30, 'U')
  
  # amenities that we are considering
  tags = {'amenity': ['food_court', 'restaurant', 'college', 'university', 'parking', 'hospital']}
  
  # fetching suitable amenity location through OpenStreetMap
  x = osmnx.geometries.geometries_from_bbox(north=lat1, south=lat, east=lon1, west=lon, tags=tags)

  x = x[['amenity']]
  x = pd.get_dummies(x['amenity'])

  possible_amenities = {
      'food_court' : 0,
      'restaurant' : 0,
      'college' : 0,
      'university': 0,
      'parking': 0, 
      'hospital': 0
 }

  captured_variables = x.columns.values.tolist()

  for amenity in captured_variables:
    if x[amenity].sum()>0:
      possible_amenities.update({amenity:1})
  
  ip_features = np.array([lat, lon, possible_amenities['college'], possible_amenities['food_court'], possible_amenities['hospital'], possible_amenities['parking'], possible_amenities['restaurant'], possible_amenities['university']])
  
  pred = new_model.predict(ip_features.reshape(-1,1).T)

  del new_model

  return pred


def round_down(num,digits):
  factor = 10.0 ** digits
  return math.floor(num * factor) / factor

@app.route('/',methods = ['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/predict',methods = ['GET', 'POST'])
def predict():
    # int_features=[int(x) for x in request.form.values()]
    # try:
        final=[float(x) for x in request.form.values()]

        prediction=predict_optimal_place(final[0],final[1])

        if(prediction == 1):
            return render_template('index.html', prediction = 'Optimal location for EV station')
        if(prediction == 0):
            return render_template('index.html', prediction = 'Not optimal location for EV station')

    # except:
    #     return render_template('index.html', prediction = 'Coordinates out of range')
        

    

if  __name__ == '__main__':
    app.run(debug=True)
