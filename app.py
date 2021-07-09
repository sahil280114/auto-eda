import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


st.set_page_config(page_title='Auto EDA', layout = 'wide', initial_sidebar_state = 'auto')
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# Web App Title
st.markdown('''
# **Auto-EDA App**
Generate commonly used descriptive statistics and plots from a csv file. Built using streamlit and pandas_profiling

---
''')

# Upload CSV data
with st.sidebar.header('Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)