import pandas as pd
# Def a function to read data
def read_data(csv_file):
    df = pd.read_csv(csv_file)
    return df