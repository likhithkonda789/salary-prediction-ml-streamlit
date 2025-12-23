import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("salary.csv")

X = df[['YearsExperience']]
y = df['Salary']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("salary_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved as salary_model.pkl")
