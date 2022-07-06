import os

def init():
    if not os.path.exists('saves'):
        os.makedirs('saves')
    if not os.path.exists('saves/save.sav'):
        with open('saves/save.sav', 'w') as f:
            f.write("")
        f.close()
        
init()

def save_variable(name, value):
    with open('saves/save.sav', 'w') as f:
        f.write(f"{name}={value}\n")
    f.close()

def read_variable(name):
    with open('./saves/save.sav', 'r') as f:
        for line in f:
            if line.startswith(name):
                return line.split('=')[1].strip()
    f.close()

def remove_variable(name):
    with open('./saves/save.sav', 'w+') as f:
        for line in f:
            if line.startswith(name):
                return f.write(line.replace(line, ''))
    f.close()

def save_data(data):
    with open('saves/save.sav', 'w') as f:
        for key, value in data.items():
            f.write(f"{key}={value}\n")
    f.close()

def read_as_data():
    data = {}
    with open('saves/save.sav', 'r') as f:
        for line in f:
            key, value = line.split('=')
            data[key] = value.strip()
    f.close()
    return data
