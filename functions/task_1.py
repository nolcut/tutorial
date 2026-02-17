import os
import json
import random

def task_1(folder='tutorial', output1='dataset1.json', output2='dataset2.json'):
    os.makedirs(folder, exist_ok=True)
    data1 = [random.uniform(0, 100) for _ in range(100)]
    data2 = [random.uniform(0, 100) for _ in range(100)]
    with open(os.path.join(folder, output1), 'w') as f1:
        json.dump(data1, f1)
    with open(os.path.join(folder, output2), 'w') as f2:
        json.dump(data2, f2)
    faasr_put_file(local_file='dataset1.json', remote_folder=folder, remote_file='dataset1.json')
    faasr_put_file(local_file='dataset2.json', remote_folder=folder, remote_file='dataset2.json')