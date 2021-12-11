import pandas as pd
import streamlit as st

DATA_URL = 'https://raw.githubusercontent.com/sivi-shahab/FTDS-HACKTIV8-Batch006/main/final_data2.csv'

@st.cache
# fungsi untuk load data
def load_data():
    dataframe = pd.read_csv(DATA_URL)
    lowercase = lambda x: str(x).lower()
    dataframe.rename(lowercase, axis='columns', inplace=True)
    return dataframe