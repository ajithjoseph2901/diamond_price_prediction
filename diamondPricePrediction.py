import streamlit as st
import pickle
import gzip

with gzip.open('model_rf_light.pkl.gz', 'rb') as file:
    model_rf_light = pickle.load(file)

st.title("Diamond Price Prediction: Input Data")

# Text Field
st.subheader("Carat")
carat = st.text_input("Enter Carat")
st.write("Carat:", carat)
st.subheader("Depth")
depth = st.text_input("Enter Depth")
st.write("Depth:", depth)
st.subheader("Table")
table = st.text_input("Enter Table")
st.write("Table:", table)
st.subheader("x")
x = st.text_input("Enter x")
st.write("x:", x)
st.subheader("y")
y = st.text_input("Enter y")
st.write("y:", y)
st.subheader("z")
z = st.text_input("Enter z")
st.write("z:", z)


# Radio Buttons
st.subheader("Cut")
cut = st.radio("Select Cut value", ["Fair","Good","Very Good","Premium","Ideal"])
st.write("Cut value:", cut)
if cut=="Fair": 
    cut=1
elif cut=="Good":
    cut=2
elif cut=="Very Good":
    cut=3
elif cut=="Premium":
    cut=4
elif cut=="Ideal":
    cut=5
st.subheader("Color")
color = st.radio("Select color", ["D","E","F","G","H","I","J"])
st.write("Color:", color)
if color=="J": 
    color=1
elif color=="I":
    color=2
elif color=="H":
    color=3
elif color=="G":
    color=4
elif color=="F":
    color=5
elif color=="E":
    color=6
elif color=="D":
    color=7

st.subheader("Clarity")
clarity = st.radio("Select Clarity", ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"])
st.write("Clarity Level:", clarity)
if clarity=="I1": 
    clarity=1
elif clarity=="SI2":
    clarity=2
elif clarity=="SI1":
    clarity=3
elif clarity=="VS2":
    clarity=4
elif clarity=="VS1":
    clarity=5
elif clarity=="VVS2":
    clarity=6
elif clarity=="VVS1":
    clarity=7
elif clarity=="IF":
    clarity=8

if st.button("Predict Price"):
    st.write("Price Predicted!")
    yhat_test = model_rf_light.predict([[float(carat),float(cut),float(color),float(clarity),
                                   float(depth),float(table),float(x),float(y),float(z)]])
    st.write("Diamond Price is $",yhat_test)

