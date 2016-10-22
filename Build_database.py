import sqlite3
import os

def Build_Database(test_data_path = './a3-data.sql'):
    conn = sqlite3.connect('./hospital.db')
    c = conn.cursor()
    c.execute(' PRAGMA forteign_keys=ON; ')
    conn.commit()

    with open('./hospital.sql', 'r') as f:  #build the database structure
            hospital_schema = f.read()    
    c.executescript(hospital_schema)
    conn.commit()
    with open(test_data_path, 'r') as f: #add the test data to the database
        test_data = f.read()
    c.executescript(test_data)
    conn.commit()
    conn.close()
    return 0

Build_Database()