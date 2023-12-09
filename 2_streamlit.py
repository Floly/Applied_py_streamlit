import streamlit as st
import pandas as pd

df = pd.read_csv('datasets/D_basic.csv', index_col=0)

st.dataframe(data=df.head(4))