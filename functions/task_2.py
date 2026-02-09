import os
import csv
import random

def task_2(folder='tutorial', output1='dataset2.csv'):
    os.makedirs(folder, exist_ok=True)
    path_out = os.path.join(folder, output1)
    with open(path_out, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['value'])
        for _ in range(20):
            writer.writerow([random.randint(0, 100)])
    faasr_put_file(local_file='dataset2.csv', remote_folder=folder, remote_file='dataset2.csv')