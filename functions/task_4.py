import os
import pandas as pd

def task_4(folder='tutorial', input1='cleaned_dataset.csv', output1='extracted_data.csv'):
    os.makedirs(folder, exist_ok=True)
    input_path = os.path.join(folder, input1)
    output_path = os.path.join(folder, output1)
    faasr_get_file(remote_folder=folder, remote_file='cleaned_dataset.csv', local_file='cleaned_dataset.csv')
    df = pd.read_csv(input_path)
    possible_precip_cols = ['PRCP', 'prcp', 'precipitation', 'Precipitation']
    possible_tmin_cols = ['TMIN', 'tmin', 'min_temperature', 'MinTemp', 'TMIN_C']
    possible_tmax_cols = ['TMAX', 'tmax', 'max_temperature', 'MaxTemp', 'TMAX_C']

    def find_col(possible_names, columns):
        for name in possible_names:
            if name in columns:
                return name
        return None
    cols = df.columns
    prcp_col = find_col(possible_precip_cols, cols)
    tmin_col = find_col(possible_tmin_cols, cols)
    tmax_col = find_col(possible_tmax_cols, cols)
    selected_cols = []
    if prcp_col:
        selected_cols.append(prcp_col)
    if tmin_col:
        selected_cols.append(tmin_col)
    if tmax_col:
        selected_cols.append(tmax_col)
    id_cols = []
    for c in ['station', 'STATION', 'id', 'ID', 'DATE', 'date']:
        if c in cols:
            id_cols.append(c)
    final_cols = id_cols + [c for c in selected_cols if c not in id_cols]
    if not final_cols:
        pd.DataFrame().to_csv(output_path, index=False)
        return
    df_extracted = df[final_cols]
    df_extracted.to_csv(output_path, index=False)
    faasr_put_file(local_file='extracted_data.csv', remote_folder=folder, remote_file='extracted_data.csv')