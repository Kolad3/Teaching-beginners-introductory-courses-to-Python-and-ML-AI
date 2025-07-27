# This code generates a synthetic dataset for study hours vs scores.
# It creates a larger dataset to be used in machine learning models for predicting student scores based on hours studied.

import pandas as pd
import numpy as np

# Generate a larger synthetic dataset for study hours vs scores
np.random.seed(42)
study_hours = np.round(np.random.uniform(1, 10, 50), 1)
scores = np.round(10 * study_hours + np.random.normal(0, 5, 50)).astype(int)  # Adding some noise

# Create DataFrame
data = pd.DataFrame({
    "Hours": study_hours,
    "Scores": scores
})

# Save to CSV
csv_path = "C:\\Users\\DELL\\Documents\\Teens Empowerment\\student_scores_large.csv"    # Path to save the generated dataset, replace with your desired path
data.to_csv(csv_path, index=False)

# Show a preview
data.head()