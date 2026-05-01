import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="ChurnSense Pro", page_icon="🚀", layout="centered")

# ---------- LOAD MODEL ----------
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# ---------- UI ----------
st.title("🚀 Customer Churn Predictor")
st.write("AI-powered churn prediction system")

# Inputs
Age = st.number_input("Age", 18, 100, 30)
Income = st.selectbox("Income", ["Low Income", "Middle Income", "High Income"])
FrequentFlyer = st.selectbox("Frequent Flyer", ["No", "Yes"])
Services = st.number_input("Services Used", 1, 10, 3)
Social = st.selectbox("Social Media Linked", ["No", "Yes"])
Hotel = st.selectbox("Booked Hotel", ["No", "Yes"])

if st.button("Predict"):

    try:
        ff = 1 if FrequentFlyer == "Yes" else 0
        sm = 1 if Social == "Yes" else 0
        ht = 1 if Hotel == "Yes" else 0

        inc = {"Low Income": 0, "Middle Income": 1, "High Income": 2}[Income]

        data = np.array([[Age, ff, inc, Services, sm, ht]])

        pred = model.predict(data)

        if pred[0] == 1:
            st.error("⚠️ High Churn Risk")
        else:
            st.success("✅ Customer Will Stay")

    except Exception as e:
        st.error(f"Error: {e}")
