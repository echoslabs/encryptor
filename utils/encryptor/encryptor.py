import cryptography
import utils.save as save
import utils.files as files
from cryptography.fernet import Fernet


def generate_key(key_dir):
    # Generates a key
    key = Fernet.generate_key()
    files.write_bytes(f"{key_dir}/key.key", key)

def encrypt(file, key, name, deleteOriginal=True):
    # Accesses the key
    f = Fernet(key)

    # Encrypts the data
    original = files.read_bytes(file)
    encrypted = f.encrypt(original)

    # Writes the encrypted data to the file
    files.write_bytes(f"{files.get_dir_by_file_name(file)}{name}", encrypted)
    
    # Deletes the original file
    if deleteOriginal:
        files.delete_file(file)

def decrypt(file, key, name, deleteEncrypted=True):
    
    # Accesses the key
    f = Fernet(key)

    # Trys to read the data of the encrypted file if fails returns an error
    try:
        encrypted_file = files.read_bytes(file)
    except FileNotFoundError:
        print("The file doesn't exist")
        return

    # Trys to decrypt the data if it fails it will return the error
    try:
        decrypted_file = f.decrypt(encrypted_file)
    except cryptography.fernet.InvalidToken:
        print("Invalid token")
        return
    except:
        print("Unknown error")

    # Writes the decrypted data to the file
    files.write_bytes(f"{files.get_dir_by_file_name(file)}{name}", decrypted_file)

    # Deletes the original file
    if deleteEncrypted:
        files.delete_file(file)
