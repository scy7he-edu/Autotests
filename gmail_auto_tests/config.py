import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class UserCredentials:
    FIRST_NAME = os.getenv('FIRST_NAME')
    LAST_NAME = os.getenv('LAST_NAME')
    BIRTH_MONTH = os.getenv('BIRTH_MONTH')
    BIRTH_DAY = os.getenv('BIRTH_DAY')
    BIRTH_YEAR = os.getenv('BIRTH_YEAR')
    GENDER = os.getenv('GENDER')
    EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
    PASSWORD = os.getenv('PASSWORD')
    RECEPIENT = os.getenv('RECEPIENT')
    MSG_SUBJECT = os.getenv('MSG_SUBJECT')
    MSG_TEXT = os.getenv('MSG_TEXT')