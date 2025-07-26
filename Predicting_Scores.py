# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 2: Load dataset
path = "C:\\Users\\DELL\\Documents\\Teens Empowerment\\student_scores_large.csv" # Path to the data file in my personal computer
data = pd.read_csv(path)  # Or upload via Colab
print(data.head())

# Step 3: Prepare features and labels
X = data[["Hours"]]
y = data["Scores"]

# Step 4: Create and train the model
model = LinearRegression()
model.fit(X, y)

# Step 5: Predict
predicted_score = model.predict([[7.5]])
print(f"Predicted score for 7.5 hours of study: {predicted_score[0]:.2f}")

# Step 6: Visualize
plt.scatter(X, y, color="blue", label="Actual Scores")
plt.plot(X, model.predict(X), color="red", label="Prediction Line")
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.title("Study Hours vs Score")
plt.legend()
plt.show()
