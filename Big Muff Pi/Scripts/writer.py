import csv
import numpy as np

toSearch= ['Refs', 'Value']

# Path to the CSV file
csv_file = 'components.csv'

# Open the CSV file and print the specified column
def obtainColumn(search):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)  # Reads the CSV into a dictionary
        # Create array.
        column= []
        for row in reader:
            #print(row[search])  # Print the value in the specified column
            column.append(row[search])
        return column

# # Open the CSV file and search for the string
# def obtainRowColumn(search_string):
#     with open(csv_file, mode='r', newline='') as file:
#         reader= csv.reader(file)
#         for row_index, row in enumerate(reader):  # Iterate through rows
#             for col_index, value in enumerate(row):  # Iterate through columns
#                     if value == search_string:  # Check if the value matches the search string
#                         #print(f"Found '{search_string}' at Row: {row_index}, Column: {col_index}")
#                         return row_index, col_index


columns= []
for search in toSearch:
    columns.append(obtainColumn(search))

print(columns)
