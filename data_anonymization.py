import numpy as np
import pandas as pd

def anonymize_data(df):
    if df.empty:
        print("No data to anonymize.")
        return df

    print("Anonymizing data...")

    df['Billing Amount'] = pd.to_numeric(df['Billing Amount'])
    df['Billing Amount'] = df['Billing Amount'] + np.random.uniform(0, 100000)

    df['Name'] = df['Name'].apply(lambda x: 'Pessoa_' + ''.join(np.random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 5)))

    if 'Age' in df.columns:
        df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
        df['Age'] = df['Age'] + np.random.randint(-5, 6, size=df.shape[0])
        df['Age'] = df['Age'].clip(lower=18, upper=100)

    return df
