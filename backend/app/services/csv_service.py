import pandas as pd

def analyze_csv(file):

    df = pd.read_csv(file)

    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "columns_list": list(df.columns),
        "missing_values": df.isnull().sum().to_dict()
    }

    return summary
