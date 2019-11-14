first_name = "Marc"
print(first_name)
print(len(first_name))
last_name = "Manley"
print(last_name)
print(len(last_name))
total_char = "Total length of characters in first and last name:"

full_name = f"{len(first_name)} {first_name} {len(last_name)} {last_name} {total_char} {len(first_name) + len(last_name)}"
print(full_name)
