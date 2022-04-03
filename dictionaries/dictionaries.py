example_dict = {"Luke": 30, "Mark": 32, "Walter": 40}

# Loop a dictionary
for name, age in example_dict.items():
    print(f"{name} is {age} years old")

# Get the keys and values in list format
dict_keys = list(example_dict.keys())
print(dict_keys)
dict_values = list(example_dict.values())
print(dict_values)

# Get a value from a dict
print(example_dict.get('Luke'))

# Modify a value of a dict
example_dict['Luke'] = 22
print(example_dict)

# Add a new item to a dict
example_dict["Peter"] = 50
print(example_dict)

# Delete an item from a dict
del example_dict["Peter"]
print(example_dict)
