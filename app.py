import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("🏠 AI House Price Predictor")
st.write("My First Live AI Project")

data = {'Size':[500,800,1000,1500,2000], 'Price':[20,35,45,70,95]}
df = pd.DataFrame(data)
model = LinearRegression()
model.fit(df[['Size']], df['Price'])

size = st.slider("Ghar ka Size (sq ft)", 300, 3000, 1000)

if st.button("Predict Karo ✨"):
    price = model.predict([[size]])[0]
    st.success(f"Predicted Price: Rs {price:.2f} Lakh")
    st.balloons()
