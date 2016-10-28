import sqlite3
import os

def Build_Database(test_data_path = './a3-data.sql'):
    conn = sqlite3.connect('./hospital.db')
    c = conn.cursor()
    
    c.execute(' PRAGMA forteign_keys=ON; ') ## WHY DOES THIS STATEMENT WORK????? foreign is mispelled, but if I spell it as foreign, I get the error: sqlite3.IntegrityError: FOREIGN KEY constraint failed
    ## Didn't find a single result on google for "Pragma forteign_keys=ON" but it's also the way it's implemented in the test file they gave us for the lab
    conn.commit()

    with open('./hospital.sql', 'r') as f:  #build the database structure
            hospital_schema = f.read()    
    c.executescript(hospital_schema)
    conn.commit()
    
    
    with open(test_data_path, 'r') as f: #add the test data to the database based on the test_data_path
        test_data = f.read()
    c.executescript(test_data)
    conn.commit()
    conn.close()
    return 0