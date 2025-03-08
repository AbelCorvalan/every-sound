import csv

# Data to write to the CSV file
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# Open the file in write mode
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the data row by row
    writer.writerows(data)

print("CSV file created successfully!")