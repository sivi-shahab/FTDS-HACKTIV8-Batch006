import streamlit as st
import seaborn as sns
from sales.dataframe import load_data

data = load_data()

def App():
    st.title('Hypothesis Testing')
    radio_button=st.radio("Pilih visualisasi", ("Jangan Tampilkan Visualisasi", "Measure of Central Tendency", "Distribution Plot"))
    if radio_button == 'Jangan Tampilkan Visualisasi':
        st.empty()
    elif radio_button == 'Measure of Central Tendency':
            df_can_col = st.selectbox("Pilih Data Total COGS Berdasarkan Kategori", ['Gender', 'Payment', 'Customer Type', 'Product Line'])
            if df_can_col == 'Payment':
                with sns.axes_style(style='ticks'):
                    g = sns.catplot(x='branch', y="cogs", hue='payment', data=data, kind="box")
                    g.set_axis_labels("Cabang Supermarket", "Total COGS");
                    st.pyplot(g)
            elif df_can_col == 'Gender':
                with sns.axes_style(style='ticks'):
                    g = sns.catplot(x='branch', y="cogs", hue='gender', data=data, kind="box")
                    g.set_axis_labels("Cabang Supermarket", "Total COGS");
                    st.pyplot(g)
            elif df_can_col == 'Customer Type':
                with sns.axes_style(style='ticks'):
                    g = sns.catplot(x='branch', y="cogs", hue='customer type', data=data, kind="box")
                    g.set_axis_labels("Cabang Supermarket", "Total COGS");
                    st.pyplot(g)
            else:
                with sns.axes_style(style='ticks'):
                    g = sns.catplot(x='branch', y="cogs", hue='product line', data=data, kind="box")
                    g.set_axis_labels("Cabang Supermarket", "Total COGS");
                    st.pyplot(g)
    elif radio_button == 'Distribution Plot':
        df_can_col = st.selectbox("Pilih Data Total COGS Berdasarkan Kategori", ['Gender', 'Payment', 'Customer Type', 'Product Line'])
        if df_can_col == 'Customer Type':
            with sns.axes_style('darkgrid'):
                h = sns.catplot(x='branch', y="cogs", hue='customer type',
                data=data, palette="muted", kind="violin")
                h.set_axis_labels("Cabang Supermarket", "Total COGS");
                st.pyplot(h)
        elif df_can_col == 'Gender':
            with sns.axes_style('darkgrid'):
                h = sns.catplot(x='branch', y="cogs", hue='gender',
                data=data, palette="muted", kind="violin")
                h.set_axis_labels("Cabang Supermarket", "Total COGS");
                st.pyplot(h)
        elif df_can_col == 'Payment':
            with sns.axes_style('darkgrid'):
                h = sns.catplot(x='branch', y="cogs", hue='payment',
                data=data, palette="muted", kind="violin")
                h.set_axis_labels("Cabang Supermarket", "Total COGS");
                st.pyplot(h)
        else:
            with sns.axes_style('darkgrid'):
                h = sns.catplot(x='branch', y="cogs", hue='product line',
                data=data, palette="muted", kind="violin")
                h.set_axis_labels("Cabang Supermarket", "Total COGS");
                st.pyplot(h)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    with st.expander("See explanation"):
        st.write("""
     What is the ANOVA Test?

An Analysis of Variance Test, or ANOVA, can be thought of as a generalization of the t-tests for more than 2 groups. The independent t-test is used to compare the means of a condition between two groups. ANOVA is used when we want to compare the means of a condition between more than two groups.

ANOVA tests if there is a difference in the mean somewhere in the model (testing if there was an overall effect), but it does not tell us where the difference is (if there is one). To find where the difference is between the groups, we have to conduct post-hoc tests.

To perform any tests, we first need to define the null and alternate hypothesis:

Null Hypothesis – There is no significant difference among the groups
Alternate Hypothesis – There is a significant difference among the groups
Basically, ANOVA is performed by comparing two types of variation, the variation between the sample means, as well as the variation within each of the samples. The below-mentioned formula represents one-way Anova test statistics.

The result of the ANOVA formula, the F statistic (also called the F-ratio), allows for the analysis of multiple groups of data to determine the variability between samples and within samples.
  
link: https://www.analyticsvidhya.com/blog/2020/06/introduction-anova-statistics-data-science-covid-python/

Cost of Goods Sold (COGS) atau Harga Pokok Penjualan (HPP) adalah peghitungan “biaya langsung” yang timbul dalam produksi barang atau jasa apa pun. Ini termasuk biaya material, biaya tenaga kerja langsung, dan biaya overhead pabrik langsung, dan berbanding lurus dengan pendapatan.
 
link: https://accurate.id/akuntansi/cogs-adalah/
 
 Uji Hipotesis rata-rata harian COGS Supermarket tiap Cabang

**H0: μ_A = μ_B =  μ_C**
**H1: μ_A != μ_B != μ_C**

Rata-Rata Cogs perhari adalah:

Daily Average of A 1136.4405617977525

Daily Average of B 1136.4116853932583

Daily Average of C 1183.185730337079

f_stat,p_value = stats.f_oneway(df_A_cogs, df_B_cogs, df_C_cogs)

print('P-value:',p_value)

output:

P-value: 0.8966510338618997

karena P-value lebih besar dari 0.05, maka kita bisa simpulkan bahwa H0 diterima artinya tidak ada perbedaan yang signifikan
Harga Pokok Penjualan setiap harinya di masing-masing cabang.


  """)