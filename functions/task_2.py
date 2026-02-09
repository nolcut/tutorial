import os
import csv
import random

def task_2(folder='tutorial', output1='random_integers_2.csv'):
    os.makedirs(folder, exist_ok=True)
    output1_path = os.path.join(folder, output1)
    random_integers = [random.randint(-100, 100) for _ in range(20)]
    with open(output1_path, mode='w', newline='') as f:
        writer = csv.writer(f)
        for val in random_integers:
            writer.writerow([val])
    faasr_put_file(local_file='random_integers_2.csv', remote_folder=folder, remote_file='random_integers_2.csv')