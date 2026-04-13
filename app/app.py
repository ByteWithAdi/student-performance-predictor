import streamlit as st
import pandas as pd
import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict_student

st.title("🎓 Student Performance Prediction System")
data = pd.read_csv('../data/student_data.csv')

st.subheader("📊 Data Overview")
st.bar_chart(data[['hours_study', 'hours_sleep']])
st.markdown("## 📊 Enter Student Details")
st.write("This app predicts whether a student will pass or fail.")

hours = st.slider("Study Hours", 0, 10)
sleep = st.slider("Sleep Hours", 0, 10)
attendance = st.slider("Attendance (%)", 0, 100)
marks = st.slider("Previous Marks", 0, 100)

if st.button("Predict"):
    result = predict_student(hours, sleep, attendance, marks)
    st.success(f"Result: {result}")
   
    if result == "Pass":
      st.success("✅ Student will Pass")
    else:
      st.error("❌ Student will Fail")
