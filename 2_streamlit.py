import streamlit as st
import pandas as pd
import plotly.express as px
from statsmodels.discrete.discrete_model import Logit

df = pd.read_csv('datasets/D_basic.csv', index_col=0)

st.markdown("Первые 4 строки датафрейма")
st.dataframe(data=df.head(4))

cols = df.columns.tolist()[2:]

with st.expander("Распределения признаков"):
    for col in cols:
        fig = px.histogram(df[col],
                        title=f'{col} DISTRIBUTION')
        st.plotly_chart(fig)

st.markdown("### Посмотрим на описательные статистики")
st.dataframe(data=df.describe())

st.markdown("### Посмотрим на матрицу корреляций")
corr_fig = px.imshow(df.iloc[:,2:].corr().round(2), text_auto=True)
st.plotly_chart(corr_fig)

feats = df.columns.tolist()[3:]
target = 'TARGET'
Xtrain = df[feats]
ytrain = df[target]
log_reg = Logit(ytrain, Xtrain).fit() 
summary = log_reg.summary2()

message = '''
    ### Попробуем выявить зависимости между признаками и таргетом
    Для этого построим логрег и посмотрим на значимость переменных
    '''
st.markdown(message)
st.markdown('Качество получившейся модели')
st.dataframe(summary.tables[0])

st.markdown('Влияние признаков на таргета')
st.dataframe(summary.tables[1])

