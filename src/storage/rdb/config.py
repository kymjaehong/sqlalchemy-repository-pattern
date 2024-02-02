""" config.py """
ASYNC_ENGINE = "mysql+mysqlconnector"
HOST = "127.0.0.1"
PORT = "3306"
NAME = "todo"
USERNAME = "root"
PASSWORD = "1234"

DATABASE_URL = f"{ASYNC_ENGINE}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{NAME}"
