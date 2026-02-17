import os
import csv
import random

def task_1(folder='tutorial', output1='final_output.csv'):
    os.makedirs(folder, exist_ok=True)
    dataset1 = [random.randint(1, 100) for _ in range(10)]
    dataset2 = [random.randint(1, 100) for _ in range(10)]
    if len(dataset1) != len(dataset2):
        raise ValueError('Data sets are not of equal length.')
    if not all((isinstance(x, (int, float)) for x in dataset1)):
        raise TypeError('Dataset1 contains non-numerical values.')
    if not all((isinstance(x, (int, float)) for x in dataset2)):
        raise TypeError('Dataset2 contains non-numerical values.')
    summed = [a + b for a, b in zip(dataset1, dataset2)]
    output_path = os.path.join(folder, output1)
    with open(output_path, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Dataset1', 'Dataset2', 'Sum'])
        for d1, d2, s in zip(dataset1, dataset2, summed):
            writer.writerow([d1, d2, s])
    faasr_put_file(local_file='final_output.csv', remote_folder=folder, remote_file='final_output.csv')