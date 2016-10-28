import sqlite3
from hashlib import sha224
from New_User_System import New_User_System
import Doctor
import Nurse
from Admin import Admin
'''
Login function returns the staff_id and role of whoever ended up logging in
'''
def Login():
    #connect to the database
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    
    login_success = False
    while login_success == False:
        print "\nEnter 'newuser' to navigate to a user entry system,\nEnter 'shutdown' to shutdown the system \nType 'exit' to exit or enter your registered login."
        login = raw_input("\nPlease enter your login: ")
        #return us to the main screen
        if login.lower() == 'exit':
            return 0,0
        #turn off the program
        if login.lower() == 'shutdown':
            return 0, 'S'
        #add a new user into the system
        if login.lower() == 'newuser':
            insertion = New_User_System()
            #return us to main screen
            if insertion == 'exit':
                return 0, 0
            # add the new user into the database, since there is so much error checking in the process, there is no way that it won't be the correct format to be entered into the database
            c.executemany("INSERT INTO staff VALUES (?,?,?,?,?)",insertion)                 #inserts user
            conn.commit()                                                                   #commits change to database
            print "\nSuccessfully added user"
            continue                                                                        #return to login segment
        
        en_pass = sha224(raw_input("Please enter your password: ")).hexdigest()             #encodes password
        
        #check if supplied username and password are from a user in the db
        c.execute("SELECT staff_id, role, name FROM staff WHERE login=:login and password=:password", {"login": login , "password": en_pass})
        row=c.fetchone()
        
        #if that pair doesn't exist in the database
        if row == None:
            print "\nError: User not in database"
            
        #if the pair does exist in the database, log them in (ie, return their staff_ID and their role)    
        else:
            print "\nLogged in as ID: " + str(row[0]) + " with role " + str(row[1])
            print "Welcome", str(row[2]), '\n'
            login_success = True
            return str(row[0]), str(row[1]) #goes back to login_system, the part where it decides which part of the system to send the user to based on their role


def Login_system():
    
    '''
    Handles logging in, passes control to Login() to get valid login information, which then returns the staff_id and role of who logged in. 
    Then it decides what to run based on the role receieved in the login process.
    '''
    while 0==0:
        #get a valid staff_id and role from the database
        staff_id, role = Login()
        #now send them to different places based on their role
        if role == 'A':
            Admin()
        elif role == 'D':
            Doctor.Doctor(staff_id, role)
        elif role == 'N':
            Nurse.Nurse(role, staff_id)
        #shutdown the system
        elif role == 'S':
            return 'Shutdown'
        #return to the main screen
        elif role == 0:
            return 0