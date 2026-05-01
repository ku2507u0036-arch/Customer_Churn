import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Churn App", layout="centered")

@st.cache_resource
def load_model():
    return pickle.load(open("model.pkl", "rb"))

model = load_model()

st.title("🚀 Customer Churn Predictor")

age = st.number_input("Age", 18, 100, 30)
income = st.selectbox("Income", ["Low Income", "Middle Income", "High Income"])
flyer = st.selectbox("Frequent Flyer", ["No", "Yes"])
services = st.number_input("Services", 1, 10, 3)
social = st.selectbox("Social Media", ["No", "Yes"])
hotel = st.selectbox("Hotel Booking", ["No", "Yes"])

if st.button("Predict"):
    try:
        ff = 1 if flyer == "Yes" else 0
        sm = 1 if social == "Yes" else 0
        ht = 1 if hotel == "Yes" else 0
        inc = {"Low Income": 0, "Middle Income": 1, "High Income": 2}[income]

        data = np.array([[age, ff, inc, services, sm, ht]])

        pred = model.predict(data)

        if pred[0] == 1:
            st.error("⚠️ High Churn Risk")
        else:
            st.success("✅ Customer Will Stay")

    except Exception as e:
        st.error(e)
