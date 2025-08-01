
# Step 1: Import tools
from sklearn.linear_model import LinearRegression

# Step 2: Prepare the data
# Our features (inputs) and labels (outputs)
ages = [[5], [7], [9], [11], [13]]
heights = [105, 120, 132, 145, 155]

# Step 3: Create the model
model = LinearRegression()

# Step 4: Train the model
model.fit(ages, heights)

# Step 5: Make a prediction
guess = model.predict([[10]])
print(f"Predicted height for age 10: {guess[0]:.2f} cm")
