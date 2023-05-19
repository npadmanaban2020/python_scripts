import os
import csv

input_directory = "C:/Users/duboue_razer/Desktop/CSV_BORIS_MOD/input"
output_directory = "C:/Users/duboue_razer/Desktop/CSV_BORIS_MOD/output"

def modify_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        
        behavior_column_index = 5  # Column F
        status_column_index = 8  # Column I
        
        rows_to_write = []
        
        for row in rows[16:]:
            behavior_value = row[behavior_column_index]
            status_value = row[status_column_index]
            if behavior_value and status_value:
                rows_to_write.append([behavior_value, status_value])
            
    output_file_path = os.path.join(output_directory, output_file)
    
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Behavior", "Status"])  # Write the header row once
        
        for row in rows_to_write:
            writer.writerow(row)  # Write the modified rows

# Iterate over CSV files in the input directory
for file_name in os.listdir(input_directory):
    if file_name.endswith('.csv'):
        input_file_path = os.path.join(input_directory, file_name)
        output_file_name = file_name.split('.csv')[0] + '_modified.csv'
        modify_csv(input_file_path, output_file_name)
        print(f"Modified file '{file_name}' and saved as '{output_file_name}' in the output directory.")
