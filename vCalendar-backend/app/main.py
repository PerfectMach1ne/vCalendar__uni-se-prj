import sqlite3
from fastapi import FastAPI

from playground.sqlite_test import create_connection

app = FastAPI()

print("please work already")  # yeeeees

if __name__ == "__main__":
    create_connection(r"D:\Programming\uni-se-prj\vCalendar-backend\database\maindb.db")
