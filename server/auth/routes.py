import secrets
import string
import hashlib
from getpass import getpass

#
USER_DETAILS_FILEPATH = "users.txt"
PUNCTUATIONS = "@#$%&"
DEFAULT_PASSWORD_LENGTH = 23

#Invalid password length message
INVALID_LENGTH_MESSAGE = f'''
Password length must be between 8 and 16
Password length must be a number:
Generating password with default length of {DEFAULT_PASSWORD_LENGTH} characters.
'''
#Generate a password
