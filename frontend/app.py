import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="AgroMind", layout="centered")

st.title("🌱 AgroMind Smart Crop Recommendation System")
st.markdown("AI-powered precision agriculture decision support")

st.divider()

# -----------------------------
# INPUT SECTION
# -----------------------------
st.header("🧪 Soil Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0.0)

with col2:
    P = st.number_input("Phosphorus (P)", min_value=0.0)

with col3:
    K = st.number_input("Potassium (K)", min_value=0.0)

ph = st.number_input("Soil pH")
city = st.text_input("📍 Enter City for Weather Data")

st.divider()

# -----------------------------
# PREDICTION BUTTON
# -----------------------------
if st.button("🌾 Predict Optimal Crop"):

    input_data = {
        "N": N,
        "P": P,
        "K": K,
        "ph": ph,
        "city": city
    }

    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            result = response.json()

            st.success(f"🌟 Recommended Crop: {result['recommended_crop']}")

            st.subheader("🌦 Weather Conditions")
            st.json(result["weather"])

            st.subheader("🧪 Soil Health Analysis")
            if isinstance(result["soil_health_report"], list):
                for item in result["soil_health_report"]:
                    st.warning(item)
            else:
                st.info(result["soil_health_report"])

        else:
            st.error("Prediction failed")

    except:
        st.error("Cannot connect to backend server")