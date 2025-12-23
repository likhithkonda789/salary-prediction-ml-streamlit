import streamlit as st
import pickle
import pandas as pd

# Load model
with open("salary_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Salary Prediction App")

experience = st.number_input(
    "Enter Years of Experience",
    min_value=0.0,
    step=0.1
)

if st.button("Predict Salary"):
    input_df = pd.DataFrame(
        [[experience]],
        columns=["YearsExperience"]
    )
    prediction = model.predict(input_df)
    st.success(f"Predicted Salary: ₹ {prediction[0]:.2f}")
