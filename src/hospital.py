import sqlite3
import sys
from Build_database import Build_Database
from utilities import parse_file, greeting
from Login import Login_system



'''
When run from terminal, type $ python2 hospital.py ./My_different_data.sql to load the database with alternate data.
if no second path is supplied, data will default to our fake test data

To run using data supplied by the TA today, run it as:

Python2 hospital.py Class_Test_Data_P1.sql

I changed some of the user's logins so that we can still use the same

#login: Nurse
#password: Npassword
#login: Admin
#password: Apassword
#login: Doctor
#password: Dpassword

thing for each of the different types of person
'''

#try logging in  with one of:

#login: Nurse
#password: Npassword
#login: Admin
#password: Apassword
#login: Doctor
#password: Dpassword

def main(argv):
    
    #takes the first command line argument as an optional path for data, if blank, then the default data is our test data
    #uses the given schema from project specifications to build the database    
    try:
        Build_Database(argv[1])
        print "building database from data at", argv[1]
    except:
        Build_Database()
        print "Built database using fake test data"
    print "\nWelcome."

    while 0 == 0:
        #greeting is a message about which option the user would like to choose, it also ensures the user only picks a valid option and then returns that answer
        answer = greeting()

        #Login
        if answer == '1':
            x = Login_system() #x will return as 'Shutdown' if the user wants to shut down the system
            if x is not None:
                if x == 'Shutdown':
                    return x
                
        #specify the path of an sql file that should be read (not for queries).
        #typical form: ./my_file.sql
        elif answer == '2':
            parse_file()

        #shut down the system entirely
        elif answer == '3':
            return 'Shutdown'


if __name__ == '__main__':
    main(sys.argv)
    print "Shutting down the system"
    print "\nGoodbye."
