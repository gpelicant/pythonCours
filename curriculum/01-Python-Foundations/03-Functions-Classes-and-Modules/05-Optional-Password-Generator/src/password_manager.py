# TODO: implement the exercices
"""
    my password generation
"""
import random
import string

def generate_password(n_characters= 20):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n_characters))

class PasswordRecord(object):
    """
        class for record password
    """
    def __init__(self, url, password=None):
        self.url = url
        self.password = password if password is not None else generate_password()

class PasswordManager(object):
    """
        class for manage password
    """
    passwords = []

    def __init__(self, passwords=[]):
        pass

    def add_password(self, value):
        if isinstance(value, PasswordRecord):
            self.passwords.append(value)
        else:
            self.passwords.append(PasswordRecord('url.com'))