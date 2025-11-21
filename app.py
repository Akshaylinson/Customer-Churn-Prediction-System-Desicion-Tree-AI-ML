import streamlit as st
import pandas as pd
import pickle

st.title("🌳 Customer Churn Prediction - Decision Tree")

model = pickle.load(open("model/churn_model.pkl", "rb"))
encoder = pickle.load(open("model/encoder.pkl", "rb"))

age = st.slider("Age", 18, 60)
gender = st.selectbox("Gender", ["Male", "Female"])
tenure = st.slider("Tenure (years)", 1, 10)
balance = st.number_input("Account Balance", 0, 300000)
num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
is_active = st.selectbox("Is Active Member?", [0, 1])
salary = st.number_input("Estimated Salary", 0, 300000)

if st.button("Predict Churn"):

    gender_enc = encoder.transform([gender])[0]

    input_data = pd.DataFrame([[
        age, gender_enc, tenure, balance, num_products, is_active, salary
    ]], columns=[
        "Age", "Gender", "Tenure", "Balance",
        "NumOfProducts", "IsActive", "EstimatedSalary"
    ])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Customer is likely to CHURN")
    else:
        st.success("✅ Customer will NOT churn")
