example_list = ["Luke", "Mark", "Walter"]
example_tuple = ("Luke", "Mark", "Walter")
example_set = {"Luke", "Mark", "Walter"}

# Assignments (ONLY IN LISTS NOT ALLOWED IN SETS AND TUPLES)
example_list[0] = "Peter"
# example_set[0] = "Peter"
# example_tuple[0] = "Peter"
print(example_list)

# Add an element (ONLY IN LISTS AND SETS). SETS COULD NOT CONTAIN DUPLICATED ELEMENTS
example_list.append("Kevin")
example_set.add("Kevin")
print(example_list)
print(example_set)

# Delete an element (ONLY IN LISTS AND SETS)
example_list.remove("Kevin")
example_set.remove("Kevin")
print(example_list)
print(example_set)

# Define a tuple with a single element
example_tuple_unique = ("Walter",)
print(example_tuple_unique)
