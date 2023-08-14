import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Load the data
data = pd.read_csv('newdata.csv')

# Step 2: Preprocess the data
features = data[['Temperature (Celcius)', 'Humidity (%)', 'THI']]
target_column = 'Status'
target = data[target_column]

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 4: Define a list of algorithms to test
algorithms = [
    ('Random Forest', RandomForestClassifier(random_state=42)),
    ('K-Nearest Neighbors', KNeighborsClassifier()),
    ('Logistic Regression', LogisticRegression(max_iter=1000)) # SVR Remove (not applicable for classification)
]

# Step 5: Test and evaluate each algorithm
for name, model in algorithms:
    print(f"Algorithm: {name}")
    
    if name == 'Logistic Regression':
        # Define hyperparameters and their ranges for grid search
        param_grid = {
            'C': [0.001, 0.01, 0.1, 1, 10, 100],
            'penalty': ['l2']
        }
        grid_search = GridSearchCV(estimator=model, param_grid=param_grid, scoring='accuracy', cv=5)
        grid_search.fit(X_train, y_train)
        best_model = grid_search.best_estimator_
        predictions = best_model.predict(X_test)
    else:
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, predictions)
    print(f"{name} Accuracy: {accuracy:.2f}")
        
    # Visualization: Plot confusion matrix (only for classification)
    from sklearn.metrics import confusion_matrix
    import seaborn as sns
        
    plt.figure(figsize=(6, 6))
    cm = confusion_matrix(y_test, predictions)
    sns.heatmap(cm, annot=True, fmt="d")
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(f'{name} Confusion Matrix')
    plt.show()
    
    print()
