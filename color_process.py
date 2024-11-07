import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#print(plt.style.available)

# Load the dataset
data = pd.read_csv("RGBSet.csv")

# Extract features and labels
X = data[['R', 'G', 'B']].values
y = data['Color'].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# KNN classifier creation. 3 nearest neighbors
knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# Model evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy with k=4:", accuracy * 100)

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

rgb_value = [218, 143, 107]  # Replace with your RGB value
predicted_color = predict_color(rgb_value)
print(f"The predicted color for RGB value {rgb_value} is {predicted_color}")