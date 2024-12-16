import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#print(plt.style.available)

# Load the dataset
data = pd.read_csv("../datasets/RGBSet.csv")

# Extract features and labels
X = data[['R', 'G', 'B']].values
y = data['Color'].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# KNN classifier creation. 3 nearest neighbors
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# app evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy with k=3:", accuracy * 100)

# Plotting the data
plt.style.use('seaborn-v0_8-dark')
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=pd.factorize(y)[0], marker='*', s=100, edgecolors='green')
legend1 = ax.legend(*scatter.legend_elements(), title="Colors")
ax.add_artist(legend1)
plt.show()

def predict_color(color):
    prediction = knn.predict([color])
    return prediction[0]

# Sample RGB values with expected colors
rgb_values = [
    [102, 7, 107],  # Expected: Purple
    [255, 0, 0],    # Expected: Red
    [0, 255, 0],    # Expected: Green
    [0, 0, 255],    # Expected: Blue
    [255, 255, 0],  # Expected: Yellow
    [0, 255, 255],  # Expected: Blue
    [255, 165, 0],  # Expected: Orange
    [128, 128, 128],# Expected: Gray
    [255, 192, 203],# Expected: Pink
    [0, 0, 0],      # Expected: Gray
    [23, 4, 100] # Expected: Blue
]

# Loop through each RGB value and predict the color
for rgb_value in rgb_values:
    predicted_color = predict_color(rgb_value)  # Ensure predict_color function is defined
    print(f"The predicted color for RGB value {rgb_value} is {predicted_color}")
