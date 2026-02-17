import os
import pandas as pd

def task_5(folder='tutorial', input1='extracted_data.csv', output1='precipitation_trends.png'):
    os.makedirs(folder, exist_ok=True)
    input_path = os.path.join(folder, input1)
    output_path = os.path.join(folder, output1)
    faasr_get_file(remote_folder=folder, remote_file='extracted_data.csv', local_file='extracted_data.csv')
    df = pd.read_csv(input_path)
    date_col_candidates = ['DATE', 'date', 'Date']
    date_col = None
    for c in date_col_candidates:
        if c in df.columns:
            date_col = c
            break
    if date_col is None:
        raise ValueError("No date column found. Expected one of: 'DATE', 'date', 'Date'.")
    prcp_candidates = ['PRCP', 'prcp', 'Precipitation', 'precipitation']
    prcp_col = None
    for c in prcp_candidates:
        if c in df.columns:
            prcp_col = c
            break
    if prcp_col is None:
        raise ValueError("No precipitation column found. Expected one of: 'PRCP', 'prcp', 'Precipitation', 'precipitation'.")
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.dropna(subset=[date_col])
    df = df.sort_values(by=date_col)
    df_agg = df.groupby(date_col, as_index=False)[prcp_col].mean()
    df_agg.to_csv(output_path, index=False)
    faasr_put_file(local_file='precipitation_trends.png', remote_folder=folder, remote_file='precipitation_trends.png')