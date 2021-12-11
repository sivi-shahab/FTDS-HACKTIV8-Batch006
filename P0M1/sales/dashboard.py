import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sales.dataframe import load_data

data = load_data()


def App():
    st.title('Visualization')
    
    data_A = data[data['branch']=='A'].groupby('date').sum()
    data_B = data[data['branch']=='B'].groupby('date').sum()
    data_C = data[data['branch']=='C'].groupby('date').sum()
    # buat column di streamlit
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Total COGS setiap hari per Cabang")
        data_A["cogs"].plot(label='Branch A')
        data_B["cogs"].plot(label='Branch B')
        data_C["cogs"].plot(label='Branch C')
        plt.legend()
        plt.title("Total COGS setiap hari di setiap cabang")
        st.pyplot()
        
    with col2:
        st.subheader("Jumlah Pengunjung Supermarket")
        sns.countplot(x ='branch', hue='gender', 
            palette = 'flare',
            data=data)
        plt.xlabel("Day")
        plt.title("Jumlah pengunjung di setiap cabang")
        st.pyplot()
        
    df_can_col = st.selectbox("Pilih Data Total COGS Berdasarkan Kategori", ['Gender', 'Payment', 'Customer Type', 'Product Line'])
    
    if df_can_col == 'Customer Type':
        sns.axes_style('darkgrid')
        plt.figure(figsize=(8, 6))
        sns.barplot(x='branch', y='cogs', hue='customer type', 
             palette = 'light:#5A9',
             data=data, ci='sd',
             capsize=0.05,
             saturation=5,
             errcolor='lightblue',
             errwidth=2)
        plt.xlabel("Branch")
        plt.ylabel("Total")
        plt.title("Total Cogs Setiap Cabang per Customer Type")
        st.pyplot()
    elif df_can_col == 'Gender':
        sns.axes_style('darkgrid')
        plt.figure(figsize=(8, 6))
        sns.barplot(x='branch', y='cogs', hue='gender', 
             palette = 'Set2',
             data=data, ci='sd',
             capsize=0.05,
             saturation=5,
             errcolor='lightblue',
             errwidth=2)
        plt.xlabel("Branch")
        plt.ylabel("Total")
        plt.title("Total Cogs Setiap Cabang per Gender")
        st.pyplot()
    elif df_can_col == 'Payment':
        sns.axes_style('darkgrid')
        plt.figure(figsize=(8, 6))
        sns.barplot(x='branch', y='cogs', hue='payment', 
             palette = 'ch:s=.25,rot=-.25',
             data=data, ci='sd',
             capsize=0.05,
             saturation=5,
             errcolor='lightblue',
             errwidth=2)
        plt.xlabel("Branch")
        plt.ylabel("Total")
        plt.title("Total Cogs Setiap Cabang per Payment")
        st.pyplot()
    else:
        sns.axes_style('darkgrid')
        plt.figure(figsize=(8, 6))
        sns.barplot(x='branch', y='cogs', hue='product line',
             data=data, ci='sd',
             capsize=0.05,
             saturation=5,
             errcolor='lightblue',
             errwidth=2)
        plt.xlabel("Branch")
        plt.ylabel("Total")
        plt.title("Total Cogs Setiap Cabang per Payment")
        st.pyplot()
# Hidden message warning because pyplot streamlit update        
st.set_option('deprecation.showPyplotGlobalUse', False)




