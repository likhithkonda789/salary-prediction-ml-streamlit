# Salary Prediction System (ML + Streamlit)

## Project Overview
This project is an end-to-end machine learning application that predicts employee salary based on years of experience. The trained model is deployed using Streamlit to provide a simple web interface for real-time predictions.

## Problem Statement
To predict an employee’s salary based on years of experience using a regression-based machine learning model and deploy it as an interactive web application.

## Dataset
The dataset contains the following fields:
- YearsExperience
- Salary

## Tools & Technologies
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

## Approach
- Loaded and explored the salary dataset
- Trained a Linear Regression model
- Saved the trained model using pickle
- Built a Streamlit web application
- Loaded the saved model to generate real-time predictions

## Model Used
- Linear Regression (Supervised Regression)

## Application Features
- User input for years of experience
- Real-time salary prediction
- Simple and interactive web interface

## How to Run
1. Install required libraries:
   ```bash
   pip install -r requirements.txt
