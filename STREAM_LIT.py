import math

import streamlit as st

import pandas as pd

import plotly.express as px
"""
 Write a function that takes the lengths of the two shorter sides of a right triangle as
 its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
 theorem, as the function’s result. Include a main program that reads the lengths of
 the shorter sides of a right triangle from the user, uses your function to compute the
 length of the hypotenuse, and displays the result.
"""
import streamlit
st.title("hypotenus")
adj = st.number_input("enter your adjacent value:", value = 0)
opp = st.number_input("enter your opposite value:", value = 0)
def hyp(a,b):
    hypo = math.sqrt(math.pow(a,2) + math.pow(b,2)) 
    return(hypo)
st.write(hyp(adj, opp))

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




"""
st.markdown("HELLO")
st.markdown("# HELLO")
st.markdown("###### HELLO")
"""



"""
import math
import streamlit as st
power = math.pow(3,4)

cosine =math.cos(45)
inv_cos = math.acos(0.5253219888177297)

st.write(cosine)

"""
"""
print(power)
"""




add = sum({14,23,25,134,23,45,78})

print(add)





"""
#list
fruits = {"mango", "apple", "cherry"}
num = {1,2,3,4,5,6}

add2 = sum(num)
print(add2)

#list
num = {3,5,6,7,8,9,4,5}

add3 = sum(num)
print(add3)
"""