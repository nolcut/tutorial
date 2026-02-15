import os
import csv
import random

def task_1(folder='tutorial', output1='dataset1.csv'):
    os.makedirs(folder, exist_ok=True)
    dataset1_path = os.path.join(folder, output1)
    data = [random.uniform(0, 100) for _ in range(20)]
    with open(dataset1_path, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['dataset1'])
        for value in data:
            writer.writerow([value])
    faasr_put_file(local_file='dataset1.csv', remote_folder=folder, remote_file='dataset1.csv')