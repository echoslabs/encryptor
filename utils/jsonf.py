import json

def write_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

def edit_keys(filename, key, value):
    with open(filename, 'r') as f:
        data = json.load(f)
    data[key] = value
    with open(filename, 'w') as f:
        json.dump(data, f)

def get_value_from_key(filename, key):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data[key]

def get_key_from_value(filename, value):
    with open(filename, 'r') as f:
        data = json.load(f)
    for key in data:
        if data[key] == value:
            return key
    return None

def remove_key(filename, key):
    with open(filename, 'r') as f:
        data = json.load(f)
    if key == data[key]:
        del data[key]