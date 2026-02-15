import os
import json

def task_4(folder='tutorial', input1='dataset1.json', input2='dataset2.json', input3='summed_dataset.json', output1='combined_output.json'):
    faasr_get_file(remote_folder=folder, remote_file='dataset1.json', local_file='dataset1.json')
    faasr_get_file(remote_folder=folder, remote_file='dataset2.json', local_file='dataset2.json')
    faasr_get_file(remote_folder=folder, remote_file='summed_dataset.json', local_file='summed_dataset.json')
    os.makedirs(folder, exist_ok=True)
    path1 = os.path.join(folder, input1)
    path2 = os.path.join(folder, input2)
    path3 = os.path.join(folder, input3)
    output_path = os.path.join(folder, output1)
    with open(path1, 'r') as f1, open(path2, 'r') as f2, open(path3, 'r') as f3:
        data1 = json.load(f1)
        data2 = json.load(f2)
        summed = json.load(f3)
    combined = {'dataset1': data1, 'dataset2': data2, 'summed_dataset': summed}
    with open(output_path, 'w') as fout:
        json.dump(combined, fout, indent=4)
    faasr_put_file(local_file='combined_output.json', remote_folder=folder, remote_file='combined_output.json')