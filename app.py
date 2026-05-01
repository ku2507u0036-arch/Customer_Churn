import streamlit as st
import pickle

st.set_page_config(page_title="ChurnSense Pro", page_icon="🚀", layout="centered")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #020617);
    font-family: 'Poppins', sans-serif;
    color: #e2e8f0;
}

/* Hide Streamlit stuff */
#MainMenu, footer, header {visibility: hidden;}

/* Title */
.title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 600;
    background: linear-gradient(90deg,#38bdf8,#a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Card */
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    margin-top: 20px;
}

/* Section */
.section {
    font-size: 0.8rem;
    color: #94a3b8;
    margin-top: 10px;
    margin-bottom: 10px;
    letter-spacing: 1px;
}

/* Button */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg,#38bdf8,#a78bfa);
    color: white;
    border-radius: 12px;
    height: 3em;
    font-weight: 600;
    border: none;
}
.stButton>button:hover {
    opacity: 0.9;
}

/* Result */
.success {
    background: rgba(34,197,94,0.1);
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #22c55e;
    text-align: center;
}
.danger {
    background: rgba(239,68,68,0.1);
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #ef4444;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOAD MODEL ----------
@st.cache_resource
def load_model():
    return pickle.load(open("model.pkl", "rb"))

model = load_model()

# ---------- HEADER ----------
st.markdown('<div class="title">🚀 ChurnSense Pro</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#94a3b8;'>Predict customer churn using AI</p>", unsafe_allow_html=True)

# ---------- INPUT CARD ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown('<div class="section">PERSONAL INFO</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    Age = st.number_input("Age", 18, 100, 30)
with col2:
    AnnualIncomeClass = st.selectbox("Income", ["Low Income", "Middle Income", "High Income"])

st.markdown('<div class="section">TRAVEL DATA</div>', unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    FrequentFlyer = st.selectbox("Frequent Flyer", ["No", "Yes"])
with col4:
    ServicesOpted = st.number_input("Services Used", 1, 10, 3)

st.markdown('<div class="section">ENGAGEMENT</div>', unsafe_allow_html=True)
col5, col6 = st.columns(2)
with col5:
    AccountSyncedToSocialMedia = st.selectbox("Social Media Linked", ["No", "Yes"])
with col6:
    BookedHotelOrNot = st.selectbox("Booked Hotel", ["No", "Yes"])

st.markdown('</div>', unsafe_allow_html=True)

# ---------- PREDICTION ----------
if st.button("🚀 Predict Churn"):

    ff = 1 if FrequentFlyer == "Yes" else 0
    asm = 1 if AccountSyncedToSocialMedia == "Yes" else 0
    bh = 1 if BookedHotelOrNot == "Yes" else 0

    inc = {
        "Low Income": 0,
        "Middle Income": 1,
        "High Income": 2
    }[AnnualIncomeClass]

    data = [[Age, ff, inc, ServicesOpted, asm, bh]]
    prediction = model.predict(data)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    if prediction[0] == 1:
        st.markdown('<div class="danger">⚠️ High Churn Risk</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="success">✅ Customer Will Stay</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
