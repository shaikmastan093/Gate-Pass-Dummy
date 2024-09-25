# mixins.py
from cryptography.fernet import Fernet

class EncryptedFieldMixin:
    def encrypt(self, value):
        fernet = Fernet(b'your-encryption-key')  # Replace with your actual key
        return fernet.encrypt(value.encode()).decode()

    def decrypt(self, value):
        fernet = Fernet(b'your-encryption-key')  # Replace with your actual key
        return fernet.decrypt(value.encode()).decode()
