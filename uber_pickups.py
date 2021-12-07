import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px




st.title("Uber pickups in NYC")
DATE_COLUMN = 'date/time'

DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data = load_data(10000)
if st.checkbox('Show raw data'):
    st.subheader("Raw Data")
    st.write(data)

st.subheader("Raw Data")


st.subheader("Number of pickups by hour")
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

st.subheader("Map of all pickups")

hour_to_filter = st.slider("hour", 0, 23, 17)
filter_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.map(filter_data)

st.subheader("Picture of a cat")

from PIL import Image
image = Image.open('kucing.jpg')

st.image(image, caption='Anak kucing')