import os
import json
import logging
import sys

def task_5(folder='tutorial', input1='validation_error.json'):
    faasr_get_file(remote_folder=folder, remote_file='validation_error.json', local_file='validation_error.json')
    os.makedirs(folder, exist_ok=True)
    error_path = os.path.join(folder, input1)
    if os.path.exists(error_path):
        with open(error_path, 'r') as f:
            error_details = json.load(f)
        logging.basicConfig(level=logging.ERROR)
        logging.error('Validation failed with error details: %s', error_details)
        sys.exit('Halting workflow due to validation failure.')