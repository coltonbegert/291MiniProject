import sqlite3
from Build_database import build_database

if __name__ == '__main__':
    sqldb = './hospital.db'
    conn = sqlite3.connect(sqldb)
    c = conn.cursor()

    build_database(conn, c)
