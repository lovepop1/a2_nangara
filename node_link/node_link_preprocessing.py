
# Step 2: Define input and output file paths
input_file_path = 'Cit-HepTh.txt'  # Replace with your actual file path
output_file_path = 'Cit-HepTh.csv'

# Step 3: Process the .txt file and save it as a .csv file
import csv
import os
import re
import pandas as pd

with open(input_file_path, 'r') as txtfile, open(output_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['FromNodeId', 'ToNodeId'])  # Write the header

    for line in txtfile:
        # Skip comment lines (starting with #)
        if line.startswith('#'):
            continue
        # Split line into two columns
        from_node, to_node = line.strip().split()
        writer.writerow([from_node, to_node])

print("Conversion complete. CSV file saved at:", output_file_path)

