import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Your dataset
data = {
    "Name": ["Aditya Pradhan", "Anjali Jena", "Krishna Singh", "Nabakrushna Singh", "Pratima Singh",
             "Kanhu Charan Singh", "Aditi Arnapurnna", "Sucheesmita Pradhan", "Kumar Pradhan",
             "Amlaan Mishra", "Sanskar Mangaraj", "Sohan Das", "Biswajit Barik", "Abhisri Das",
             "Ghanalata Das", "Bulu Swain", "Tushar Singh", "Soubhagya Muduli", "Biswa Panda",
             "Sriraj Biswal", "Tulu Agrasingh", "Sujit Goswami", "Anil Kumar Mallick", "DK Lakra",
             "Suvendu Patry", "Yashraj Yashobant Dash"],
    "Voltage by NIR Glucometer": [0.81, 1.01, 3.24, 3.61, 2.87, 2.61, 1.5, 0.85, 0.68, 1.62, 0.61,
                                  0.78, 0.65, 1.48, 0.65, 0.71, 1.58, 1.38, 1.51, 1.36, 0.87, 0.82,
                                  1.58, 0.62, 0.85, 0.76],
    "Reading by Glucometer": [86, 89, 134, 143, 119, 111, 95, 87, 81, 99, 74, 85, 75, 95, 77, 79,
                              97, 91, 97, 90, 86, 84, 99, 73, 87, 82]
}

# Create DataFrame
df = pd.DataFrame(data)

# Prepare data for training
X = df[['Voltage by NIR Glucometer']]
y = df['Reading by Glucometer']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'glucose_model.pkl')
