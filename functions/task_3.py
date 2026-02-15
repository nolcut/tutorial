import os
import csv

def task_3(folder='tutorial', input1='dataset1.csv', input2='dataset2.csv', output1='combined_output.csv'):
    faasr_get_file(remote_folder=folder, remote_file='dataset1.csv', local_file='dataset1.csv')
    faasr_get_file(remote_folder=folder, remote_file='dataset2.csv', local_file='dataset2.csv')
    os.makedirs(folder, exist_ok=True)
    path1 = os.path.join(folder, input1)
    path2 = os.path.join(folder, input2)
    out_path = os.path.join(folder, output1)
    with open(path1, newline='') as f1, open(path2, newline='') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)
        next(reader1, None)
        next(reader2, None)
        data1 = [float(row[0]) for row in reader1 if row]
        data2 = [float(row[0]) for row in reader2 if row]
    combined = [(d1, d2, d1 + d2) for d1, d2 in zip(data1, data2)]
    with open(out_path, 'w', newline='') as fout:
        writer = csv.writer(fout)
        writer.writerow(['dataset1', 'dataset2', 'sum'])
        writer.writerows(combined)
    faasr_put_file(local_file='combined_output.csv', remote_folder=folder, remote_file='combined_output.csv')