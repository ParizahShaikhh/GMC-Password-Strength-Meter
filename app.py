# Imports

import re
import streamlit as st

# Set up our app
st.set_page_config(page_title="Data Sweeper", layout="wide")

# Title
st.title("🔐 Password Strength Meter")
st.write("Check the strength of your password and get suggestions for improvement.")
def check_password_strength(password):
    score = 0
    feedback_list = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback_list.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback_list.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback_list.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback_list.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", "green", []
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "orange", feedback_list
    else:
        return "❌ Weak Password - Improve it using the suggestions below.", "red", feedback_list

# Get user input
password = st.text_input("Enter your password: ", type="password") # secure input

if password:
    strength_msg, color, feedback_list = check_password_strength(password)

    st.markdown(f"<p style='color: {color};'>{strength_msg}</p>", unsafe_allow_html=True)

    if feedback_list:
        st.warning("⚠️ Suggestions to improve your password:")
        for tip in feedback_list:
            st.write("-" + tip)
