import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("model.pkl")

st.title("📊 Customer Churn Prediction App")
st.write("Enter customer details below to predict whether they will churn.")

# User inputs
gender = st.selectbox("Gender", ["Female", "Male"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (Months)", min_value=0, max_value=72, value=1)
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0, value=100.0)

# Label encoding mappings
gender_map = {"Female": 0, "Male": 1}
partner_map = {"No": 0, "Yes": 1}
dependents_map = {"No": 0, "Yes": 1}
phone_map = {"No": 0, "Yes": 1}
multiple_map = {"No": 0, "Yes": 1, "No phone service": 2}
internet_map = {"DSL": 0, "Fiber optic": 1, "No": 2}
online_map = {"No": 0, "Yes": 1, "No internet service": 2}
contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
paperless_map = {"No": 0, "Yes": 1}
payment_map = {
    "Electronic check": 0,
    "Mailed check": 1,
    "Bank transfer (automatic)": 2,
    "Credit card (automatic)": 3,
}

# Apply mappings
input_dict = {
    "gender": gender_map[gender],
    "SeniorCitizen": SeniorCitizen,
    "Partner": partner_map[Partner],
    "Dependents": dependents_map[Dependents],
    "tenure": tenure,
    "PhoneService": phone_map[PhoneService],
    "MultipleLines": multiple_map[MultipleLines],
    "InternetService": internet_map[InternetService],
    "OnlineSecurity": online_map[OnlineSecurity],
    "OnlineBackup": online_map[OnlineBackup],
    "DeviceProtection": online_map[DeviceProtection],
    "TechSupport": online_map[TechSupport],
    "StreamingTV": online_map[StreamingTV],
    "StreamingMovies": online_map[StreamingMovies],
    "Contract": contract_map[Contract],
    "PaperlessBilling": paperless_map[PaperlessBilling],
    "PaymentMethod": payment_map[PaymentMethod],
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges,
}

df = pd.DataFrame([input_dict])

# Prediction
if st.button("Predict Churn"):
    pred = model.predict(df)[0]
    if pred == 1:
        st.error("⚠️ This customer is likely to **Churn**.")
    else:
        st.success("✅ This customer is **Not Likely to Churn**.")
