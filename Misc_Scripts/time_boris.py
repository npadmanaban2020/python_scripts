# Export events in BORIS as tabular events, save as CSV. Modify each CSV file to only have the columns "Behavior" and "Status". If doing for a large amount of BORIS videos, contact me and I can make a script for it.

import csv
import os

# set input and output file paths
input_file_path = "C:/Users/duboue_razer/Documents/test_boris.csv"
output_dir_path = "output"
output_file_path = os.path.join(output_dir_path, "output.txt")

# create output directory if it does not exist
if not os.path.exists(output_dir_path):
    os.makedirs(output_dir_path)

# open input file for reading
with open(input_file_path, 'r') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)  # convert reader object to list of rows

# process data and write to output file
with open(output_file_path, 'w') as outfile:
    for behavior in ['Bottom', 'Top', 'Freezing', 'Normal Swimming', 'Fast Swimming', 'Floor Skimming', 'Normal Turning', 'Erratic Turning', 'Wall Bumping']:
        behavior_output = []
        for row in rows:
            if row['Behavior'] == behavior and row['Status'] == 'START':
                start_time = float(row['Time'])
            elif row['Behavior'] == behavior and row['Status'] == 'STOP':
                stop_time = float(row['Time'])
                behavior_output.append(f'({start_time}, {stop_time})')
                start_time = None
        if behavior_output:
            outfile.write(f'{behavior}: {", ".join(behavior_output)}\n\n')
