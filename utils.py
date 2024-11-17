import json
import os
from dotenv import load_dotenv

def load_config():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        print("Configuration loaded successfully.")

        return config
    except FileNotFoundError:
        print("config.json file not found.")

        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding config.json: {e}")

        return None

def load_env_variables():
    load_dotenv()

    DB_USER = os.getenv("SOURCE_DB_USER")
    DB_PASSWORD = os.getenv("SOURCE_DB_PASSWORD")
    DB_HOST = os.getenv("SOURCE_DB_HOST")
    DB_PORT = os.getenv("SOURCE_DB_PORT")
    DB_SERVICE_NAME = os.getenv("SOURCE_DB_SERVICE_NAME")

    return {
        "DB_USER": DB_USER,
        "DB_PASSWORD": DB_PASSWORD,
        "DB_HOST": DB_HOST,
        "DB_PORT": DB_PORT,
        "DB_SERVICE_NAME": DB_SERVICE_NAME
    }
