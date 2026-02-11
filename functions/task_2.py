import os
import pandas as pd
import numpy as np

def task_2(folder='tutorial', input1='dataset1.csv', input2='dataset2.csv', output1='summed_dataset.csv'):
    os.makedirs(folder, exist_ok=True)
    length = 100
    data1 = pd.DataFrame(np.random.randint(0, 100, size=length), columns=['value'])
    data2 = pd.DataFrame(np.random.randint(0, 100, size=length), columns=['value'])
    data1.to_csv(os.path.join(folder, input1), index=False)
    data2.to_csv(os.path.join(folder, input2), index=False)
    faasr_get_file(remote_folder=folder, remote_file='dataset1.csv', local_file='dataset1.csv')
    faasr_get_file(remote_folder=folder, remote_file='dataset2.csv', local_file='dataset2.csv')
    df1 = pd.read_csv(os.path.join(folder, input1))
    df2 = pd.read_csv(os.path.join(folder, input2))
    summed = df1['value'] + df2['value']
    pd.DataFrame(summed, columns=['value']).to_csv(os.path.join(folder, output1), index=False)
    faasr_put_file(local_file='summed_dataset.csv', remote_folder=folder, remote_file='summed_dataset.csv')