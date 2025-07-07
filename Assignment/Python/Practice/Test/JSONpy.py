import os
os.chdir(r"C:\\paras\\Assignment\\Python\\Practice\\Test")

import json

# 1. json.dump() - Serialize Python object to JSON and write to file
# Syntax: json.dump(obj, fp, *, indent=None)
# Parameters:
#   - obj: The Python object to be serialized (e.g., dictionary, list).
#   - fp: A file-like object where the serialized JSON will be written.
#   - indent: The number of spaces to use for indentation in the JSON file.

data = {'name': 'Alice', 'age': 30}
with open('data.json', 'w') as f:
    # Writing the Python object (data) to the file as JSON with indentation
    json.dump(data, f, indent=4)


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# 2. json.dumps() - Serialize Python object to JSON string
# Syntax: json.dumps(obj, indent=None)
# Parameters:
#   - obj: The Python object to be serialized.
#   - indent: If not None, pretty-print the JSON with the given number of spaces.
data = {'name': 'Alice', 'age': 30}
json_string = json.dumps(data, indent=4)
print("Serialized JSON string:")
print(json_string)
print("---")


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# 3. json.load() - Deserialize JSON data from file into Python object
# Syntax: json.load(fp, /, *, object_hook=None) * mtlb uske bad ke sare parameter key-value pair me hi dene pdege -- aur jab / use krte he to uske aage ke sab parameter single value deni he
# Parameters:
#   - fp: A file-like object containing JSON data.
#   - object_hook: If specified, will convert JSON objects into a custom Python object.
with open('data.json', 'r') as f:
    data_from_file = json.load(f)
    print("Deserialized data from file:")
    print(data_from_file)
print("---")


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# 4. json.loads() - Deserialize JSON string into Python object
# Syntax: json.loads(s, /, *, object_hook=None)    * mtlb uske bad ke sare parameter key-value pair me hi dene pdege -- aur jab / use krte he to uske aage ke sab parameter single value deni he
# Parameters:
#   - s: A string containing JSON data to be deserialized.
#   - object_hook: If specified, will convert JSON objects into a custom Python object.
json_string = '{"name": "Alice", "age": 30}'
data_from_string = json.loads(json_string)
print("Deserialized data from JSON string:")
print(data_from_string)
print("---")


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# Example for handling more advanced features of JSON functions:

# 5. Custom Handling of Non-Serializable Objects (using `default`)
# The `default` parameter allows custom serialization of Python objects that are not natively serializable.
# You need to provide a function that handles the serialization of custom objects.
# Syntax: json.dumps(obj, default=custom_encoder)
# Parameters:
#   - obj: The Python object to be serialized.
#   - default: A function that handles the serialization of non-serializable objects.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_encoder(obj):
    if isinstance(obj, Person):
        return {"name": obj.name, "age": obj.age}
    raise TypeError(f"Type {type(obj)} not serializable")

# Create an instance of Person
person = Person("John", 40)

# Serialize the Person object using a custom encoder function
person_json = json.dumps(person, default=person_encoder)
print("Serialized custom Person object:")
print(person_json)
print("---")


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


# 6. Handling JSON with sorted keys (using `sort_keys`)
# The `sort_keys` parameter sorts dictionary keys in the serialized JSON string.
# Syntax: json.dumps(obj, indent=4, sort_keys=True)
# Parameters:
#   - sort_keys: If True, the dictionary keys will be sorted alphabetically in the output.
sorted_json = json.dumps(data, indent=4, sort_keys=True)
print("Serialized JSON with sorted keys:")
print(sorted_json)





# 1. json.dump() - Serialize Python object to JSON and write to file
# Syntax: json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, 
#                  allow_nan=True, indent=None, separators=None, default=None, 
#                  sort_keys=False, **kw)
# Parameters:
#   - obj: The Python object to be serialized (e.g., dictionary, list).
#   - fp: A file-like object where the serialized JSON will be written.
#   - indent: The number of spaces to use for indentation in the JSON file.
#   - skipkeys: If True, skip non-serializable keys.
#   - ensure_ascii: If True, escape non-ASCII characters in the JSON output.
#   - sort_keys: If True, sort dictionary keys alphabetically.