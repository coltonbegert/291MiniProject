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

#try logging in  with 
#login: Nurse
#password: Npassword

def main(argv):
    try:
        Build_Database(argv[1])
        print "building database from data at", argv[1]
    except:
        Build_Database()
    while 0 == 0:
        staff_id, role = Login()
        if role == 'A':
            pass
            #Admin(staff_id)
        elif role == 'D':
            pass
            #Doctor(staff_id)
        elif role == 'N':
            Nurse(staff_id)
        else:
            print "staff role error. Role received:", role
            return -1
            
      
if __name__ == '__main__':
    message = main(sys.argv)
    if message == -1:
        '''
        role was incorrect after login procedure
        '''
    