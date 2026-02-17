import os
import pandas as pd

def task_6(folder='tutorial', input1='extracted_data.csv', output1='min_temperature_trends.png'):
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
    tmin_candidates = ['TMIN', 'tmin', 'TMin', 't_min', 'min_temperature', 'MinTemp', 'mintemp']
    tmin_col = None
    for c in tmin_candidates:
        if c in df.columns:
            tmin_col = c
            break
    if tmin_col is None:
        raise ValueError('No minimum temperature column found. Expected one of common TMIN names.')
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.dropna(subset=[date_col, tmin_col])
    df = df.sort_values(by=date_col)
    if df[tmin_col].abs().median() > 80:
        df[tmin_col] = df[tmin_col] / 10.0
    daily = df.groupby(date_col, as_index=False)[tmin_col].mean()
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError:
        daily.to_csv(output_path.replace('.png', '_data.csv'), index=False)
        return
    faasr_put_file(local_file='min_temperature_trends.png', remote_folder=folder, remote_file='min_temperature_trends.png')
    plt.figure(figsize=(10, 5))
    plt.plot(daily[date_col], daily[tmin_col], label='Minimum Temperature', color='tab:blue')
    plt.xlabel('Date')
    plt.ylabel('Minimum Temperature (°C)')
    plt.title('Minimum Temperature Trends Over Time')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()