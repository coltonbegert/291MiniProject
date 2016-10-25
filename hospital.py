import sqlite3
import sys
from hashlib import sha224
from Build_Database import Build_Database
from Login import Login
from Nurse import Nurse


#from Admin import Admin
#from Doctor import Doctor


'''
When run from terminal, type $ python2 hospital.py ./My_different_data.sql to load the database with alternate data.
if no second path is supplied, data will default to our fake test data
'''

#try logging in  with one of:

#login: Nurse
#password: Npassword
#login: Admin
#password: Apassword
#login: Doctor
#password: Dpassword

def main(argv):
    try:
        Build_Database(argv[1])
        print "building database from data at", argv[1]
    except:
        Build_Database()
    print "\n\nWelcome."

    while 0 == 0:
        prompt = "\nWhat would you like to do?\
        \n(1) Login\
        \n(2) Add data\
        \n(3) Shutdown\n: "
        answer = raw_input( prompt )
        if answer not in ['1', '2', '3']:
            answer = raw_input( prompt)            
            
        if answer == '1':
            staff_id, role = Login()
            if role == 'A':
                pass
                #Admin(staff_id)
                
            # Needs to be implemented as 'A' --> Admin(staff_ID) and ('D', 'N') ---> Care_Staff(role, staff_ID) as per the requirements
            elif role == 'D':
                pass
                #Doctor(staff_id)
            elif role == 'N':
                Nurse(staff_id)
            elif role == 'S':
                return 0
                
        elif answer == '2':
            sql_file_path = raw_input("Please enter the path of the sql document you would like to run: ")
            if sql_file_path is not '':
                while sql_file_path.replace(' ', '')[0] != '.':
                    print "Format must be ./sql_document.sql"
                    sql_file_path = raw_input("Please enter the path of the sql document you would like to run: ")
                    
                conn = sqlite3.connect('./hospital.db')
                c = conn.cursor()                
                try:
                    with open(sql_file_path, 'r') as f:  #build the database structure
                        lines = f.read()
                    c.executescript(lines)
                    conn.commit()
                    print "Successfully ran file"
                except:
                    print "There was an error processing your request"
                
        elif answer == '3':
            return 0
            
      
if __name__ == '__main__':
    main(sys.argv)
    print "Shutting down the system"
    print "\nGoodbye."
    