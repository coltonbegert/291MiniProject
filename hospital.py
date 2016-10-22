import sqlite3
import sys
from Build_Database import Build_Database
'''
When run from terminal, type $ python2 hospital.py ./My_different_data.sql to load the database with alternate data.
if no second path is supplied, data will default to our fake test data
'''
def main(argv):
    if len(argv) > 1:
        Build_Database(argv[1])
    else:
        Build_Database()
        
if __name__ == '__main__':
    main(sys.argv)