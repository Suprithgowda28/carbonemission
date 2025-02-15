import streamlit as st
import joblib

# Load trained model
model = joblib.load("carbon_emission_model.pkl")

st.title("CarbonTracker: AI-Powered Carbon Emission Estimator")

# User input fields
runtime = st.number_input("Enter runtime in seconds:", min_value=1)
power = st.number_input("Enter power consumption in watts:", min_value=1.0)
hardware_type = st.selectbox("Select hardware:", ["CPU", "GPU", "TPU"])

# Convert hardware type to numeric
hardware_mapping = {"CPU": 0, "GPU": 1, "TPU": 2}
hardware_code = hardware_mapping[hardware_type]

# Predict button
if st.button("Estimate CO₂ Emissions"):
    prediction = model.predict([[runtime, power, hardware_code]])[0]
    st.write(f"Estimated CO₂ Emission: {prediction:.2f} grams")
