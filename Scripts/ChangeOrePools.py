import json

# Load the data from the file
input_file = 'orepools-100.json'
output_file = 'orepools-100modified.json'

# Function to multiply all ore values by 10
def multiply_ore_values(data):
    for ore_type, territories in data.items():
        for territory, amount in territories.items():
            # Multiply each ore amount by 10
            territories[territory] = amount * 10
    return data

# Read the original JSON data
with open(input_file, 'r') as f:
    ore_data = json.load(f)

# Multiply all ore values by 10
modified_data = multiply_ore_values(ore_data)

# Write the modified data back to a new file
with open(output_file, 'w') as f:
    json.dump(modified_data, f, indent=4)

print(f"Ore values have been multiplied by 10 and saved to {output_file}")
