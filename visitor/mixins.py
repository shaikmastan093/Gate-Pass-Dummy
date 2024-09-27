# mixins.py
from django.conf import settings
from cryptography.fernet import Fernet

class EncryptedFieldMixin:
    def encrypt(self, value):
        if isinstance(value, int):  # Convert integer to string
            value = str(value)
        fernet = Fernet(settings.FERNET_KEY)
        return fernet.encrypt(value.encode()).decode()

    def decrypt(self, value):
        fernet = Fernet(settings.FERNET_KEY)
        return fernet.decrypt(value.encode()).decode()
