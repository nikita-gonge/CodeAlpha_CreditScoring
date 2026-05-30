import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="Credit Scoring System",
    page_icon="💳",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color: #eef4ff;
}

h1 {
    color: #0f172a !important;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

st.sidebar.header("📊 Model Details")

st.sidebar.success("Algorithm: Logistic Regression")

st.sidebar.info("Accuracy: 51%")

st.sidebar.write("Dataset Size: 1000 Records")

st.sidebar.write("Features Used: 10")

st.sidebar.markdown("---")

st.sidebar.header("👩‍💻 Developed By")

st.sidebar.write("Nikita Gonge")

# Title
st.markdown("""
<style>

.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <h1 style='text-align:center; color:#0f172a; font-size:42px; font-weight:bold;'>
    💳 Credit Scoring Prediction System
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h3 style='text-align:center; color:#4338ca; font-size:34px; font-weight:600;'>
    Enter Customer Financial Details
    </h3>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align:center; color:#334155; font-size:18px;'>
    This ML model predicts whether a customer has Good Credit or Bad Credit.
    </p>
    """,
    unsafe_allow_html=True
)

# User Inputs
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("👤 Age", min_value=18, max_value=100)
    credit_amount = st.number_input("💰 Credit Amount")
    sex = st.selectbox(
    "👨 Sex",
    ["Male", "Female"]
)

saving_account = st.selectbox(
    "🏦 Saving Account",
    ["little", "moderate", "quite rich", "rich"]
)

with col2:
    job = st.selectbox(
        "💼 Job",
        [
            "0 - Unskilled",
            "1 - Semi Skilled",
            "2 - Skilled",
            "3 - Highly Skilled"
        ]
    )

    duration = st.number_input("📅 Duration (Months)")
    housing = st.selectbox(
    "🏠 Housing",
    ["own", "rent", "free"]
)

checking_account = st.selectbox(
    "💳 Checking Account",
    ["little", "moderate", "rich"]
)
purpose = st.selectbox(
    "🎯 Purpose",
    [
        "car",
        "radio/TV",
        "education",
        "business",
        "furniture/equipment"
    ]
)

# Prediction Button

job_mapping = {
    "0 - Unskilled": 0,
    "1 - Semi Skilled": 1,
    "2 - Skilled": 2,
    "3 - Highly Skilled": 3
}

sex_mapping = {
    "Male": 1,
    "Female": 0
}

housing_mapping = {
    "own": 1,
    "rent": 2,
    "free": 0
}

saving_mapping = {
    "little": 1,
    "moderate": 2,
    "quite rich": 3,
    "rich": 4
}

checking_mapping = {
    "little": 1,
    "moderate": 2,
    "rich": 3
}

purpose_mapping = {
    "car": 1,
    "radio/TV": 2,
    "education": 3,
    "business": 4,
    "furniture/equipment": 5
}
sex_value = sex_mapping[sex]
housing_value = housing_mapping[housing]
saving_value = saving_mapping[saving_account]
checking_value = checking_mapping[checking_account]
purpose_value = purpose_mapping[purpose]

job_value = job_mapping[job]

if st.button("🔮 Predict Credit Score"):

    input_data = np.array([[
    0,
    age,
    sex_value,
    job_value,
    housing_value,
    saving_value,
    checking_value,
    credit_amount,
    duration,
    purpose_value
]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Good Credit")

    else:
        st.error("❌ Bad Credit")

st.markdown("""
<div style='text-align:center;
color:#334155;
font-size:16px;
padding-top:5px;'>
Made with ❤️ using Streamlit | Nikita Gonge
</div>
""", unsafe_allow_html=True)