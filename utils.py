import pandas as pd
import numpy as np

def generate_dataset():

    np.random.seed(42)

    data = {
        "Age": np.random.randint(18, 60, 1000),
        "Gender": np.random.choice(["Male", "Female"], 1000),
        "Tenure": np.random.randint(1, 10, 1000),
        "Balance": np.random.randint(1000, 200000, 1000),
        "NumOfProducts": np.random.randint(1, 5, 1000),
        "IsActive": np.random.choice([0, 1], 1000),
        "EstimatedSalary": np.random.randint(30000, 200000, 1000),
    }

    df = pd.DataFrame(data)

    # Generate churn with slightly realistic pattern
    df["Churn"] = np.where(
        (df["IsActive"] == 0) & (df["Balance"] < 50000) & (df["NumOfProducts"] == 1),
        1,
        0,
    )

    return df
