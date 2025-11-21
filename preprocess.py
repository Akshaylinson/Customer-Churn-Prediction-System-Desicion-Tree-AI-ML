import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

def preprocess(df):

    encoder = LabelEncoder()
    df["Gender"] = encoder.fit_transform(df["Gender"])

    # Save encoder
    with open("model/encoder.pkl", "wb") as f:
        pickle.dump(encoder, f)

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    return X, y
