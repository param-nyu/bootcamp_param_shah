import os
from dotenv import load_dotenv  # type: ignore


def load_secrets():
    load_dotenv()
    print("Secrets loaded.")


def get_key(key_name='API_KEY'):
    return os.getenv(key_name)
