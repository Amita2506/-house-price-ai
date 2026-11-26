import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="AI House Price Predictor Pro", page_icon="🏠")

st.title("🏠 AI House Price Predictor - Pro")
st.write("My Level 2 AI Project by Amita!")

data = {'Size':[500,800,1000,1500,2000], 'Price':[20,35,45,70,95]}
df = pd.DataFrame(data)
model = LinearRegression()
model.fit(df[['Size']], df['Price'])

size = st.slider("Ghar ka Size (sq ft)", 500, 5000, 1000)

location = st.selectbox("Location chuno", ["Athagarh", "Bhubaneswar", "Cuttack", "Delhi", "Mumbai"])
rooms = st.selectbox("Kitne Rooms?", [1, 2, 3, 4, 5])
bathroom = st.selectbox("Bathroom?", [1, 2, 3])

if st.button("Predict Karo ✨"):
    price = model.predict([[size]])[0]
    
    location_extra = {"Athagarh": 0, "Bhubaneswar": 10, "Cuttack": 5, "Delhi": 40, "Mumbai": 60}
    price = price + location_extra[location] + (rooms*5) + (bathroom*2)
    
    st.success(f"📍 {location} me {size} sq ft, {rooms} BHK ka ghar")
    st.success(f"Predicted Price: Rs {price:.2f} Lakh")
    st.balloons()
