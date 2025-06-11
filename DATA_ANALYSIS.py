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

st.title("Data_Graph")
fig = px.histogram(le, x='Going_outside', title = 'graph')
st.plotly_chart(fig, use_container_width=True)

st. title("Data_Graph 2")
Personality_Count = df["Personality"]
Personality_Count.coloumns = ["Personality", "Count"]
fig2 = px.bar(Personality_Count, x='Personality', title=("graph"))
st.plotly_chart(fig2, use_container_width=True)



 
