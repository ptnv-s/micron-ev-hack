# Micron Hackathon
## Problem Statement :

Optimal Deployment of Electric Vehicles & Charging Stations

## Objective:

Design an algorithm which will tell you where to deploy charging stations in a city. Some examples of inputs to your algorithm will be traffic on that route, connectivity of the route (inner city v/s highway), presence of other charging stations nearby, installation of types of charging station (fast v/s battery swapping v/s …) etc 

## File Structure:
1. app_dir - contains code for the deployed application
 - index.html - Code for front end of the applicTION
 - app.py - Backend/API Logic for the application
 - final_ev.csv - FInal Preprocessed Extracted Data
 - optimal_pred_model3.pkl - saved xgboost model for predcition

2. data_extraction - contains script for data extraction
3. ml_models - contains logic for the algorithms and models used 

## Tech Stack:
### Front-End:
 - HTML
 - CSS
 - Bootstrap

### Back-End: 
 - Flask

### Data Engineering/ Scraping:
 - OpenStreetMap
 - OpenChargeMap
 - Geopandas

### ML-Models/Miscellenaeous : 
 - Folium
 - Numpy
 - Pandas
 - Scipy
 - XGBOOST

## Proposed Solution:

 - Recommendation of Optimal EV Charging Points in the neighbourhood area of the location given by the user as input.
