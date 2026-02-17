import os
import csv

def task_2(folder='tutorial', input1='ghcnd_dataset.csv', output1='consistent_dataset.csv'):
    faasr_get_file(remote_folder=folder, remote_file='ghcnd_dataset.csv', local_file='ghcnd_dataset.csv')
    os.makedirs(folder, exist_ok=True)
    input_path = os.path.join(folder, input1)
    output_path = os.path.join(folder, output1)
    if not os.path.exists(input_path):
        with open(output_path, 'w', newline='', encoding='utf-8') as f_out:
            pass
        return
    with open(input_path, 'r', encoding='utf-8', newline='') as f_in:
        sample = f_in.read(4096)
        f_in.seek(0)
        try:
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(sample)
            has_header = sniffer.has_header(sample)
        except csv.Error:
            dialect = csv.excel
            has_header = True
        reader = csv.reader(f_in, dialect)
        rows = list(reader)
    if not rows:
        with open(output_path, 'w', newline='', encoding='utf-8') as f_out:
            pass
        return
    if has_header:
        header = rows[0]
        data_rows = rows[1:]
    else:
        max_len = max((len(r) for r in rows))
        header = [f'col_{i + 1}' for i in range(max_len)]
        data_rows = rows
    num_cols = len(header)
    normalized_rows = []
    for row in data_rows:
        row = [field.strip() if isinstance(field, str) else field for field in row]
        if len(row) < num_cols:
            row = row + [''] * (num_cols - len(row))
        elif len(row) > num_cols:
            row = row[:num_cols]
        normalized_rows.append(row)
    with open(output_path, 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerows(normalized_rows)
    faasr_put_file(local_file='consistent_dataset.csv', remote_folder=folder, remote_file='consistent_dataset.csv')