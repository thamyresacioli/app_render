import pandas as pd 

def read_and_process_data(path):
    df = pd.read_csv(path)
    df = df.dropna(subset=['odometer', 'model_year'])
    return df