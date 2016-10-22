include sqlite3
from build_database include build_database

if __name__ == '__main__':
    sqldb = 'hospital.db'
    conn, c = connect(sqldb)

    build_database(c)
