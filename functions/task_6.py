import os
import json
import csv

def task_6(folder='tutorial', input1='summed_data.csv', input2='validation_error.json'):
    faasr_get_file(remote_folder=folder, remote_file='summed_data.csv', local_file='summed_data.csv')
    faasr_get_file(remote_folder=folder, remote_file='validation_error.json', local_file='validation_error.json')
    path_csv = os.path.join(folder, input1)
    path_json = os.path.join(folder, input2)
    if os.path.exists(path_csv):
        print(f'Workflow completed successfully. Output CSV file located at: {path_csv}')
    elif os.path.exists(path_json):
        with open(path_json, 'r') as f:
            error_details = json.load(f)
        print('Workflow failed. Validation error details:')
        print(json.dumps(error_details, indent=2))
    else:
        print('No output files found. Workflow status unknown.')