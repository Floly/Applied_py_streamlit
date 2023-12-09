import streamlit as st
import pandas as pd
import plotly.express as px
# import polars
import seaborn as sns

df = pd.read_csv('datasets/D_basic.csv', index_col=0)
first_line = '**Hello!** This is my first streamlit project :balloon:'
target_distribution = px.histogram(df['TARGET'])


st.markdown(body=first_line)

st.markdown(body="Первые 4 строки датафрейма")
st.dataframe(data=df.head(4))

cols = df.columns.tolist()[2:]

with st.expander("Распределения признаков"):
    for col in cols:
        fig = px.histogram(df[col],
                        title=f'{col} DISTRIBUTION')
        st.plotly_chart(fig)

st.markdown("### Посмотрим на матрицу корреляций")
corr_fig = px.imshow(df.iloc[:,2:].corr().round(2), text_auto=True)
st.plotly_chart(corr_fig)

# with st.expander("Распределения признаков"):
#     for col in cols:
#         fig = px.histogram(df[col],
#                         title=f'{col} DISTRIBUTION')
#         st.plotly_chart(fig)

st.markdown("### Посмотрим на описательные статистики")
st.dataframe(data=df.describe())