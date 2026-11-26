import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Amita's Premium AI", page_icon="🏠")

st.title("🏠 AI House Price Predictor - PREMIUM")
st.markdown("### My Level 3 AI Project by Amita! ✨")

# Sidebar
st.sidebar.header("Ghar ki Details")
size = st.sidebar.slider("Ghar ka Size (sq ft)", 500, 5000, 1000)
location = st.sidebar.selectbox("Location chuno", ["Delhi", "Mumbai", "Bangalore", "Pune", "Jaipur"])
bhk = st.sidebar.number_input("Kitne Rooms?", 1, 10, 2)
bath = st.sidebar.number_input("Bathroom?", 1, 5, 2)

# Price Logic
base_price = {"Delhi": 9000, "Mumbai": 18000, "Bangalore": 8000, "Pune": 7000, "Jaipur": 5000}
price = (size * base_price[location] + bhk*500000 + bath*300000) / 100000

if st.button("Predict Karo ✨"):
    st.balloons()
    st.success(f"📍 {location} me {size} sq ft, {bhk} BHK ka ghar")
    st.markdown(f"## Predicted Price: Rs {price:.2f} Lakh")
    
    # GRAPH
    st.subheader("📊 Price Comparison")
    cities = ["Delhi", "Mumbai", "Bangalore", "Pune", "Jaipur"]
    prices = [(size * base_price[c] + bhk*500000 + bath*300000)/100000 for c in cities]
    
    fig, ax = plt.subplots()
    colors = ['red' if c==location else 'skyblue' for c in cities]
    ax.bar(cities, prices, color=colors)
    ax.set_ylabel("Price in Lakh")
    st.pyplot(fig)
    st.info("Red wala tumhara selected city hai!")

st.write("Made with ❤️ by Amita")
