import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(page_title="Churn Predictor", layout="centered")

# Load model
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# UI
st.title("🚀 Customer Churn Predictor")

st.write("Enter customer details below:")

age = st.number_input("Age", 18, 100, 30)
income = st.selectbox("Income", ["Low Income", "Middle Income", "High Income"])
flyer = st.selectbox("Frequent Flyer", ["No", "Yes"])
services = st.number_input("Services Used", 1, 10, 3)
social = st.selectbox("Social Media Linked", ["No", "Yes"])
hotel = st.selectbox("Booked Hotel", ["No", "Yes"])

# Prediction
if st.button("Predict"):
    try:
        ff = 1 if flyer == "Yes" else 0
        sm = 1 if social == "Yes" else 0
        ht = 1 if hotel == "Yes" else 0
        inc = {"Low Income": 0, "Middle Income": 1, "High Income": 2}[income]

        data = np.array([[age, ff, inc, services, sm, ht]])

        prediction = model.predict(data)

        if prediction[0] == 1:
            st.error("⚠️ High Churn Risk")
        else:
            st.success("✅ Customer Will Stay")

    except Exception as e:
        st.error(f"Error: {e}")
