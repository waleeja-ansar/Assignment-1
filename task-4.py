sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys_to_extract = ["name", "salary"]

new_dict = {}
for key in keys_to_extract:
    if key in sample_dict:
        new_dict[key] = sample_dict[key]

print("New dictionary:", new_dict)