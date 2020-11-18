import json # Import JSON library

# JSON Writer & Formatter
# Written by James Barnett

file_name = str(input("JSON File Name: ")) + ".json" # Assign a file name to the json database
file = open(file_name, "x") # Create the file based on the file name
file = open(file_name, "w") # Overwrite mode for the file

temp_obj = {} # Create the temporary object dictionary
columns = int(input("Amount of columns: ")) # Determine amount of columns
for x in range(columns): # For Range of columns
    row_items = [] # Define row-items list
    column_name = str(input("Column Name: ")) # Define specific column name
    for y in range(int(input("Row amount: "))): # Loop through row list
        row_items.append(str(input("Input {}: ".format(y+1)))) # Append row items to list
    temp_obj[column_name] = row_items # Create the column and row

file.write(json.dumps(temp_obj)) # Write the temporary object to the json file
file.close() # Close the JSON file

print("JSON File Complete!") # Print JSON file message
