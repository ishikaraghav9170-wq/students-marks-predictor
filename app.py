import streamlit as st
import joblib

model = joblib.load("linear_regression_model.pkl")


st.title("Student Marks Predictor")

hours = st.number_input(
    "Enter your study hours:",
    min_value=0.0,
    max_value=24.0,
    step=1.0
)

prediction = model.predict([[hours]])
st.write("Predicted Marks:", prediction[0])