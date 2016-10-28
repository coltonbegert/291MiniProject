import sqlite3
from hashlib import sha224
'''
If you implement exit in the other functions then you can change these to those ones, otherwise, leave that alone
'''

def New_User_System():
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    while 0==0:
        print "\n\nAdding New User\nIf at any point you want to exit, just type 'exit'\nYou may use the word exit in things, but by itself it will exit"
        '''
        ID
        '''
        staff_id = raw_input("\nEnter desired Staff ID: ")
        if staff_id.lower() == 'exit':
            return 'exit'

        c.execute("SELECT * FROM staff WHERE staff_id=? ", (staff_id, ))      #if the ID is in the DB already, this will return the info on that person
        row = c.fetchone()

        #staff ID must be at most 5 characters that are numbers and the id can't already exist
        #if "row" is None that means that there were no users with that ID in the db as the last execute statement would have found one
        while len(staff_id) > 5 or row != None or staff_id.isdigit() is False:

            if len(staff_id) > 5: print "ID must be shorter than 6 characters"
            if row != None: print "Staff with that ID already exists"
            if staff_id.isdigit() is False: print "ID must be composed of numbers"

            staff_id = raw_input("Enter desired Staff ID (5 digits): ")

            if staff_id.lower() == 'exit':
                return 'exit'

            c.execute("SELECT * FROM staff WHERE staff_id=? ", (staff_id, ))
            row = c.fetchone()

        '''
        ROLE
        '''
        role = raw_input("\nEnter desired role: ").upper()
        if role.lower() == 'exit':
            return 'exit'

        #ensures the role is either D, A or N, if it is entered as lowercase, it is changed to uppercase
        while role not in ['D', 'A', 'N']:
            print "Please enter a role from 'D', 'A', 'N'"
            role = raw_input("Enter desired role (D, N, A): ").upper()
            if role.lower() == 'exit':
                return 'exit'

        '''
        NAME
        '''
        name = raw_input("\nEnter desired name: ").title() #title method capitalizes the first letter of each word and makes all others lowercase 'cOlToN bEGErT'.title() --> 'Colton Begert'
        if name.lower() == 'exit':
            return 'exit'

        #name must be less than 16 characters and can't contain numbers
        while len(name) > 15 or name.replace(' ', '').isalpha() is False:                # replace takes "John Oliver" and turns it into "JohnOliver" as isalpha doesn't like spaces
            if len(name) > 15: print "Name too long, must be shorter than 16 characters"
            if name.replace(' ', '').isalpha() is False: print "Name must not contain numbers"

            name = raw_input("Enter desired name: ").title()
            if name.lower() == 'exit':
                return 'exit'

        '''
        LOGIN
        '''
        login = raw_input("\nEnter desired login: ")
        if login.lower() == 'exit':
            return 'exit'

        #login must be less than 9 characters
        while len(login) > 8:
            print "Login must be shorter than 9 characters."
            login = raw_input("Enter desired login: ")
            if login.lower() == 'exit':
                return 'exit'
        '''
        PASSWORD
        '''
        password = sha224(raw_input("\nEnter desired password: ")).hexdigest()           # encodes entered password
        accept = raw_input("Do you want to accept these changes (Y/N/exit)?: ")          # if Y, then user is inserted, if N then it starts the new user process again
        if accept.lower() == 'exit':
            return 'exit'
        if accept.lower() == 'y':
            insertion = [(staff_id, role, name, login, password)]
            return insertion

# New_User_System()
