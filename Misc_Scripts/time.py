import os
import csv

# Create a dictionary to store the start and end times in seconds for each behavior
behavior_times = {}

# Open the CSV file
with open('C:/Users/duboue_razer/Documents/test.csv', 'r') as file:
    reader = csv.DictReader(file)

    # Iterate over each row in the file
    for row in reader:
        # Check if Start_time field is empty
        if not row['Start_time']:
            continue
        
        # Convert the start time to seconds
        start_time_seconds = (int(row['Start_time'][:2]) * 60) + float(row['Start_time'][3:])
        
        # Convert the end time to seconds
        end_time_seconds = (int(row['End_time'][:2]) * 60) + float(row['End_time'][3:])
        
        # Store the start and end times in seconds for this behavior in the dictionary
        if row['Event'] in behavior_times:
            behavior_times[row['Event']].append((start_time_seconds, end_time_seconds))
        else:
            behavior_times[row['Event']] = [(start_time_seconds, end_time_seconds)]

# Create the output directory if it does not exist
if not os.path.exists('output'):
    os.mkdir('output')

# Write the results to a text file in the output directory
with open('output/behavior_times.txt', 'w') as file:
    for behavior in behavior_times:
        file.write(behavior + '\n')
        for time_range in behavior_times[behavior]:
            file.write('(' + str(time_range[0]) + ', ' + str(time_range[1]) + '), ')
        file.write('\n')
