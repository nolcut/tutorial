import os
import csv
import random

def task_2(folder='tutorial', output1='dataset2.csv'):
    os.makedirs(folder, exist_ok=True)
    data1 = [random.uniform(0, 100) for _ in range(100)]
    data2 = [random.uniform(0, 100) for _ in range(100)]
    output_path = os.path.join(folder, output1)
    with open(output_path, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['value'])
        for val in data2:
            writer.writerow([val])
    faasr_put_file(local_file='dataset2.csv', remote_folder=folder, remote_file='dataset2.csv')