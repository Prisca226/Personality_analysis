import pandas as pd


import streamlit as st

import plotly.express as px
st.title("PERSONALITY")
#create a data frame
df = pd.read_csv("personality_dataset.csv")
#st.table(df)


#code for data inspection
st.markdown("### FIRST 5 DATA")
pa = df.head(5)
st.write(pa)

st.markdown("### LAST 5 DATA")
we = df.tail(5)
st.write(we)

st.markdown("### DATA INFO")
my = df.info()
st.write(my)

st.markdown("### DATA DESCRIBE")
my = df.describe()
st.write(my)

st.markdown("### DATA SHAPE")
my = df.shape
st.write(my)



st.markdown("# UNIVARIATE ANALYSIS")
so = df['Post_frequency'].describe()
st.write(so)

no = df['Time_spent_Alone'].describe()
st.write(no)

le = df['Going_outside'].describe()
st.write(le)

no = df['Social_event_attendance'].describe()
st.write(no)

no = df['Friends_circle_size'].describe()
st.write(no)






 
