# config_encryptor/key_manager.py

import os
from cryptography.fernet import Fernet

def generate_key(file_path='secret.key'):
    """
    Generate and store an encryption key in a file.
    """
    key = Fernet.generate_key()
    os.environ['CONFIG_ENCRYPTION_KEY'] = key.decode()
    return key

def load_key():
    """
    Load the encryption key from an environment variable or file.
    """
    key = os.getenv('CONFIG_ENCRYPTION_KEY')

    if key:
        return key.encode()
    else:
       raise ValueError("No encryption key found in environment")
