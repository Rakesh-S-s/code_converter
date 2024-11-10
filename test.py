# Specify the file path
file_path = 'converted_py.py'

# Open the file and read all lines
with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove the first and last lines
lines = lines[1:-1]

# Write the modified content back to the file
with open(file_path, 'w') as file:
    file.writelines(lines)

print("First and last lines removed successfully.")
