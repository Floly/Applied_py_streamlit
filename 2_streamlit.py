import streamlit as st
import pandas as pd

df = pd.read_csv('datasets/D_basic.csv', index_col=0)
first_line = 'Hello! This is my first streamlit project :balloon:'

st.markdown(body=first_line)
st.dataframe(data=df.head(4))