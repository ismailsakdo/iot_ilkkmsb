import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Load the data
data = pd.read_csv('newdata.csv')
data.describe()

# Step 2: Preprocess the data
features = data[['Temperature (Celcius)', 'Humidity (%)']]
target_column = 'Status'
target = data[target_column]

# Step 3: Define a list of algorithms to test
algorithms = [
    ('Random Forest', RandomForestClassifier(random_state=42)),
    ('SVM', SVC(random_state=42)),
    ('K-Nearest Neighbors', KNeighborsClassifier()),
    ('Logistic Regression', LogisticRegression(random_state=42))
]

# Step 4: Test and evaluate each algorithm
for name, model in algorithms:
    print(f"Algorithm: {name}")
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy: {accuracy:.2f}")
    print()
