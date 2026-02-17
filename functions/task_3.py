import os
import json

def task_3(folder='tutorial', input1='datasets_validated.json', output1='summed_data.json'):
    faasr_get_file(remote_folder=folder, remote_file='datasets_validated.json', local_file='datasets_validated.json')
    os.makedirs(folder, exist_ok=True)
    input_path = os.path.join(folder, input1)
    output_path = os.path.join(folder, output1)
    with open(input_path, 'r') as f:
        data = json.load(f)
    dataset1 = data.get('dataset1')
    dataset2 = data.get('dataset2')
    if not isinstance(dataset1, list) or not isinstance(dataset2, list):
        raise ValueError('Both dataset1 and dataset2 must be lists.')
    if len(dataset1) != len(dataset2):
        raise ValueError('dataset1 and dataset2 must be of equal length.')
    summed = [a + b for a, b in zip(dataset1, dataset2)]
    with open(output_path, 'w') as f:
        json.dump(summed, f)
    faasr_put_file(local_file='summed_data.json', remote_folder=folder, remote_file='summed_data.json')