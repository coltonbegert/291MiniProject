import sqlite3
from Build_database import build_database

if __name__ == '__main__':
    sqldb = './hospital.db'
    conn, c = connect(sqldb)

    build_database(c)
