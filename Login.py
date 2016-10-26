import sqlite3
from hashlib import sha224
from New_User_System import New_User_System
'''
Login function returns the staff_id and role of whoever ended up logging in
'''
def Login():
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    login_success = False
    while login_success == False:
        print "\nEnter 'newuser' to navigate to a user entry system,\nEnter 'shutdown' to shutdown the system \nType 'exit' to exit or enter your registered login."
        login = raw_input("\nPlease enter your login: ")
        if login.lower() == 'exit':
            return 0,0
        if login.lower() == 'shutdown':
            return 0, 'S'
        if login.lower() == 'newuser':
            insertion = New_User_System()
            if insertion == 'exit':
                return 0, 0
            
            c.executemany("INSERT INTO staff VALUES (?,?,?,?,?)",insertion)                 #inserts user
            conn.commit()                                                                   #commits change to database
            print "\nSuccessfully added user"                                               # to be totally sure, this could perform a database search for the new user to ensure they've been added, probably unnecessary
            continue                                                                        #return to login segment
        
        en_pass = sha224(raw_input("Please enter your password: ")).hexdigest()             #encodes password
        #check if supplied username and password are from a user in the db
        c.execute("SELECT staff_id, role, name FROM staff WHERE login=:login and password=:password", {"login": login , "password": en_pass})
        row=c.fetchone()
        if row == None:
            print "\nError: User not in database"
        else:
            print "\nLogged in as ID: " + str(row[0]) + " with role " + str(row[1])
            print "Welcome", str(row[2])
            login_success = True
            return str(row[0]), str(row[1])
