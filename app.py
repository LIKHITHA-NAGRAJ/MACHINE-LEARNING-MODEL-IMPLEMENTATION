import streamlit as st
import pickle
import requests
from datetime import datetime
import json
import os

# ---------- Set page config FIRST ----------
st.set_page_config(page_title="Spam Detector & Holiday Checker", page_icon="📩", layout="wide")

# ---------- Load the spam model and vectorizer ----------
@st.cache_resource
def load_model():
    with open("spam_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = load_model()

# ---------- Styling ----------
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
    }
    .stTextArea textarea {
        background-color: #1e1e2f;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Sidebar Navigation ----------
st.sidebar.title("🛠️ Navigation")
page = st.sidebar.radio("Choose a page:", ["📩 Spam Classifier", "📅 Holiday Checker (India)"])

# ---------- Spam Classifier ----------
if page == "📩 Spam Classifier":
    st.title("📩 SMS Spam Classifier")
    st.write("Enter a message below and the model will classify it as Spam or Not Spam.")

    user_input = st.text_area("💬 Type your message:")

    if st.button("🔍 Predict"):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter a message.")
        else:
            input_vector = vectorizer.transform([user_input])
            prediction = model.predict(input_vector)[0]
            confidence = model.predict_proba(input_vector)[0][prediction]

            if prediction == 1:
                st.error(f"🚫 Spam ({confidence * 100:.2f}% confidence)")
            else:
                st.success(f"✅ Not Spam ({confidence * 100:.2f}% confidence)")

    st.markdown("#### 📌 Try these Spam messages:")
    spam_examples = [
        "Congratulations! You’ve won a free iPhone. Click here to claim now.",
        "URGENT: Your account is suspended. Login now to verify.",
        "You have been selected for a $1000 Walmart gift card.",
        "Free entry in 2 a weekly competition to win tickets to Maldives."
    ]
    for example in spam_examples:
        st.code(example)

# ---------- Holiday Checker ----------
# ---------- Holiday Checker ----------
elif page == "📅 Holiday Checker (India)":
    st.title("📅 Indian Holiday Checker")
    st.write("Check if a specific date is a public holiday or weekend in India using real-time data or fallback info.")

    selected_date = st.date_input("📅 Choose a date to check:", datetime.today())
    selected_str = selected_date.strftime('%Y-%m-%d')
    current_year = selected_date.year

    fallback_data = [
        {"date": "2025-01-26", "localName": "Republic Day"},
        {"date": "2025-08-15", "localName": "Independence Day"},
        {"date": "2025-10-02", "localName": "Gandhi Jayanti"},
        {"date": "2025-11-01", "localName": "Kannada Rajyotsava"},
        {"date": "2025-12-25", "localName": "Christmas Day"},
    ]

    holidays = []
    used_fallback = False
    try:
        response = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{current_year}/IN", timeout=5)
        if response.status_code == 200:
            holidays = response.json()
            with open("holidays.json", "w", encoding="utf-8") as f:
                json.dump(holidays, f, indent=4, ensure_ascii=False)
        elif response.status_code == 204:
            st.markdown(
                "<div style='font-size: 12px; color: gray; text-align: right;'>⚠️ Using fallback holiday data (API returned 204)</div>",
                unsafe_allow_html=True
            )
            debug = st.sidebar.checkbox("🔧 Show debug info", value=False)
            if debug:
                st.warning("⚠️ No holiday data available from the API (204 No Content). Using fallback data.")

            holidays = fallback_data
            used_fallback = True
        else:
            st.error("❌ Failed to fetch holiday data from API. Using fallback.")
            holidays = fallback_data
            used_fallback = True
    except Exception as e:
        st.warning(f"⚠️ Network/API error: {e}")
        st.info("📁 Loading fallback holiday list...")
        holidays = fallback_data
        used_fallback = True

    # Check if selected date is a weekend
    is_weekend = selected_date.weekday() in [5, 6]  # Saturday = 5, Sunday = 6
    selected_holiday = next((h for h in holidays if h["date"] == selected_str), None)

    # Display results
    if selected_holiday:
        st.success(f"🎉 {selected_str} is a public holiday: **{selected_holiday['localName']}**")
    elif is_weekend:
        weekend_name = "Saturday" if selected_date.weekday() == 5 else "Sunday"
        st.info(f"🛌 {selected_str} is a weekend: **{weekend_name}**")
    else:
        st.info(f"📅 {selected_str} is not a public holiday or weekend.")

    # Show fallback holidays if API failed
    if used_fallback:
        st.markdown("### 📅 Upcoming Fallback Holidays")
        for h in fallback_data:
            if h["date"] >= selected_str:
                st.markdown(f"📌 **{h['date']}**: {h['localName']}")



# ---------- Footer ----------
st.markdown(
    """
    <br><hr>
    <center>🚀 CODTECH Internship Task 4 | Built with Streamlit, Scikit-learn & Nager API</center>
    """,
    unsafe_allow_html=True
)
