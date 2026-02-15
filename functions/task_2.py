import os
import csv

def task_2(folder='tutorial', input1='dataset1.csv', input2='dataset2.csv', output1='combined_output.csv'):
    faasr_get_file(remote_folder=folder, remote_file='dataset1.csv', local_file='dataset1.csv')
    faasr_get_file(remote_folder=folder, remote_file='dataset2.csv', local_file='dataset2.csv')
    os.makedirs(folder, exist_ok=True)
    path1 = os.path.join(folder, input1)
    path2 = os.path.join(folder, input2)
    out_path = os.path.join(folder, output1)
    data1 = []
    data2 = []
    with open(path1, newline='') as f1:
        reader1 = csv.reader(f1)
        for row in reader1:
            if row:
                try:
                    data1.append(float(row[0]))
                except ValueError:
                    pass
    with open(path2, newline='') as f2:
        reader2 = csv.reader(f2)
        for row in reader2:
            if row:
                try:
                    data2.append(float(row[0]))
                except ValueError:
                    pass
    combined = [(d1, d2, d1 + d2) for d1, d2 in zip(data1, data2)]
    with open(out_path, 'w', newline='') as fout:
        writer = csv.writer(fout)
        writer.writerow(['Dataset1', 'Dataset2', 'Sum'])
        writer.writerows(combined)
    faasr_put_file(local_file='combined_output.csv', remote_folder=folder, remote_file='combined_output.csv')