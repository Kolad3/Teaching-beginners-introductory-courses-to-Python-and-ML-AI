import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression 

# Step 2: Load Dataset 
path = "C:\\Users\\DELL\\Documents\\Teens Empowerment\\student_scores_large.csv"
data = pd.read_csv(path)

#Step 3: Prepare the features and labels 
X = data[['Hours']]
y = data['Scores']

# Step 4: Create the model 
model = LinearRegression()
model.fit(X,y)

# Step 5: Make prediction 
predicted_score = model.predict([[7.5]])
print(f'Predicted score for 7.5 hours of study: {predicted_score[0]:.2f}')

# Step 6 Visualize 
plt.scatter(X, y, color='blue', label='Actual Scores')
plt.plot(X , model.predict(X), color='red', label='Predicted Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')
plt.title('Study Hours vs Scores')
plt.legend()
plt.show()