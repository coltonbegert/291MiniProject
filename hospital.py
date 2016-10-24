import sqlite3
import sys
from hashlib import sha224
from Build_Database import Build_Database

'''
When run from terminal, type $ python2 hospital.py ./My_different_data.sql to load the database with alternate data.
if no second path is supplied, data will default to our fake test data
'''
def main(argv):
    try:
        Build_Database(argv[1])
        print "building database from data at", argv[1]
    except:
        Build_Database()
    
    '''
    login function should be seperate and return the staff_id and role of whoever ended up logging in
    '''
    
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    
    login_success = False
    while login_success != True:
        print "\nEnter 'newuser' to navigate to a user entry system"
        login = raw_input("Please enter your login: ")
        
        if login.lower() == 'newuser':
            accept = 'N'
            while accept.lower() != 'y':
                print "\n\nAdding New User"
                '''
                ID
                '''
                staff_id = raw_input("\nEnter desired Staff ID: ")
                formatting = (staff_id, )                                           #haaaate the formatting here, but couldn't do it any other way (to my knowledge)
                c.execute("SELECT * FROM staff WHERE staff_id=? ", formatting)      #if the ID is in the DB already, this will return the info on that person
                row = c.fetchone()
                
                #staff ID must be at most 5 characters that are numbers and the id can't already exist
                #if "row" is None that means that there were no users with that ID in the db as the last execute statement would have found one
                while len(staff_id) > 5 or row != None or staff_id.isdigit() is False:
                    if len(staff_id) > 5:
                        print "ID can't be longer than 5 characters"
                    if row != None:
                        print "Staff with that ID already exists"
                    if staff_id.isdigit() is False:
                        print "ID not composed of numbers"
                    staff_id = raw_input("Enter desired Staff ID (5 digits): ")
                    formatting = (staff_id, )
                    c.execute("SELECT * FROM staff WHERE staff_id=? ", formatting)
                    row = c.fetchone()                   
                    
                '''
                ROLE
                '''
                role = raw_input("\nEnter desired role: ").upper()
                
                #ensures the role is either D, A or N, if it is entered as lowercase, it is changed to uppercase
                while role not in ['D', 'A', 'N']:
                    print "Please enter a role from 'D', 'A', 'N'"
                    role = raw_input("Enter desired role (D, N, A): ").upper()
                
                '''
                NAME
                '''
                name = raw_input("Enter desired name: ").title() #title method capitalizes the first letter of each word and makes all others lowercase 'cOlToN bEGErT'.title() --> 'Colton Begert'

                #name must be less than 16 characters and can't contain numbers
                while len(name) > 15 or name.replace(' ', '').isalpha() is False:                # replace takes "John Oliver" and turns it into "JohnOliver" as isalpha doesn't like spaces
                    if len(name) > 15:
                        print "Name too long, must be shorter than 16 characters"
                    if name.replace(' ', '').isalpha() is False:
                        print "Name contains numbers"
                    name = raw_input("Enter desired name: ").title()
                
                '''
                LOGIN
                '''
                login = raw_input("\nEnter desired login: ")
                
                #login must be less than 9 characters
                while len(login) > 8:
                    print "Login must be shorter than 9 characters."
                    name = raw_input("Enter desired login: ")
                '''
                PASSWORD
                '''
                password = sha224(raw_input("Enter desired password: ")).hexdigest()        # immediately encodes entered password
                accept = raw_input("Do you want to accept these changes (Y/N)?: ")          # if Y, then user is inserted, if N then it starts the new user process again
                
            insertion = [(staff_id, role, name, login, password)]
            c.executemany("INSERT INTO staff VALUES (?,?,?,?,?)",insertion)                 #inserts user
            conn.commit()                                                                   #commits change to database
            continue                                                                        #return to login segment
        
        en_pass = sha224(raw_input("Please enter your password: ")).hexdigest()             #encodes password
        #check if supplied username and password are from a user in the db
        c.execute("SELECT staff_id, role, name FROM staff WHERE login=:login and password=:password", {"login": login , "password": en_pass})
        row=c.fetchone()
        if row == None:
            print "\nError: User not in database"
        else:
            print "logged in as ID: " + str(row[0]) + " with role " + str(row[1]) + ", and name is " + str(row[2])
            login_success = True
        
      
if __name__ == '__main__':
    main(sys.argv)