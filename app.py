import streamlit as st
import requests
from datetime import datetime, time, timezone


'''
# New York Taxi Fare Prediction API
'''

st.markdown('''
## **Journey Details**
''')

pickup_date = st.date_input(
     "Pickup Date?",
     value=datetime(2021, 2, 26))
pickup_time = st.time_input(
    'Pickup time?',
    value=time(6, 30))

pickup_datetime = f'{pickup_date} {pickup_time} UTC'
st.write(pickup_datetime)

pickup_longitude = st.text_input(
        'Pickup longitude?',
        value=40.7614327)
pickup_latitude = st.text_input(
        'Pickup latitude?',
        value=-73.9798156)
dropoff_longitude = st.text_input(
        'Pickup latitude?',
        value=40.6413111)
dropoff_latitude = st.text_input(
        'Pickup latitude?',
        value=-73.9797156)

coords = "Pickup Coordinates = {}, {}, \n\nDropoff Coordinates= {}, {}".format(pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude)
st.write(coords)


passenger_count = st.slider('Number of Passengers', 1, 6, 2)

''' ## **Fare Prediction** '''

url = 'https://taxifare-2fufqv4ora-ew.a.run.app/predict_fare/'
params = dict(
  key='2012-10-06 12:10:20.0000001',
  pickup_datetime=pickup_datetime,
  pickup_longitude=pickup_longitude,
  pickup_latitude=pickup_latitude,
  dropoff_longitude=dropoff_longitude,
  dropoff_latitude=dropoff_latitude,
  passenger_count=passenger_count
)

prediction = round(float(requests.get(url, params).json()['prediction']), 2)

res = f'Your fare is predicted to be around ${prediction}'
st.write(res)
