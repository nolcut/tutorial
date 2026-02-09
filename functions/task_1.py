import os
import csv
import random

def task_1(folder='tutorial', output1='dataset1.csv'):
    os.makedirs(folder, exist_ok=True)
    path1 = os.path.join(folder, output1)
    with open(path1, mode='w', newline='') as f1:
        writer = csv.writer(f1)
        writer.writerow(['value'])
        for _ in range(20):
            writer.writerow([random.randint(0, 100)])
    faasr_put_file(local_file='dataset1.csv', remote_folder=folder, remote_file='dataset1.csv')