import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def loadknn():
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
    return knn

def predict_color(knn, color):
    prediction = knn.predict(color)
    return prediction[0]

if __name__ == '__main__':
    knn = loadknn()
    x = [[78, 167, 241]]  # Input as a 2D array
    result = predict_color(knn, x)
    print("Predicted Color:", result)
