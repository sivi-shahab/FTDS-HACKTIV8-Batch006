import streamlit as st
from multiapp import MultiApp
from sales import dashboard, hipotesis


st.title('Supermarket Sales Dashboard')

st.write('Historical record of sales data in 3 different supermarkets')

st.sidebar.file_uploader("Upload a file", type=['csv', 'txt'])


app = MultiApp() 

# Add all your application here
app.add_app('Visualization', dashboard.App)
app.add_app('Hypothesis Testing', hipotesis.App)

# The main app
app.run()

