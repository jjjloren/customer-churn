import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('models/best_churn_model.pkl')

st.title("📊 Customer Churn Prediction Dashboard")

st.write("Enter customer details below to predict if they will churn:")

# Example input fields
gender = st.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=1)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=500.0)

# Convert inputs into a DataFrame
input_data = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [senior_citizen],
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges]
})

# Predict
if st.button("Predict Churn"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("❌ This customer is likely to churn.")
    else:
        st.success("✅ This customer is likely to stay.")
