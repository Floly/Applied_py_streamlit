import streamlit as st
import pandas as pd

df = pd.read_csv('datasets/D_basic.csv')

st.dataframe(data=df)