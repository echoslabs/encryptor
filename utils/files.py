import os

def write_file(file, data):
    with open(file, 'w') as f:
        f.write(f"{data}")
    f.close()

def write_bytes(file, data):
    with open(file, 'wb') as f:
        f.write(data)
    f.close()

def open_file(file):
    open(file, 'w+')

def read_file(file):
    with open(file, 'r') as f:
        data = f.read()
    f.close()
    return data

def read_bytes(file):
    with open(file, 'rb') as f:
        data = f.read()
    f.close()
    return data

def rename_file(file, new_name):
    os.rename(file, new_name)

def get_dir_by_file_name(file):
    return os.path.dirname(file)

def delete_file(file):
    os.remove(file)

def clear_file(file):
    write_file(file, '')

def file_exists(file):
    return os.path.isfile(file)

def dir_exists(dir):
    return os.path.isdir(dir)

def create_file(file):
    open(file, 'w').close()

def append_file(file, data):
    with open(file, 'a') as f:
        f.write(data)
    f.close()

def create_dir(dir):
    os.mkdir(dir)

def delete_dir(dir):
    os.rmdir(dir)

def clear_dir(dir):
    for file in os.listdir(dir):
        os.remove(file)
        
def list(dir):
    return os.listdir(dir)

def get_file_size(file):
    return os.path.getsize(file)

def get_file_name(file):
    return os.path.basename(file)

def get_file_extension(file):
    return os.path.splitext(file)[1]

