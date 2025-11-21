import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
from utils import generate_dataset
from preprocess import preprocess

def train():

    # Generate dataset
    df = generate_dataset()
    df.to_csv("data/churn_data.csv", index=False)

    # Preprocess
    X, y = preprocess(df)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    # Save model
    with open("model/churn_model.pkl", "wb") as f:
        pickle.dump(model, f)

    pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, pred))
    print(classification_report(y_test, pred))

if __name__ == "__main__":
    train()   # This is correct
