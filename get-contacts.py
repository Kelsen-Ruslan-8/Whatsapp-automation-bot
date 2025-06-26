import pandas as pd
def get_contacts(csv_path):
    df = pd.read_csv(csv_path)
    return df.to_dict(orient='records')
