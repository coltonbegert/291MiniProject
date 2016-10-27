import sqlite3
from Login import Login
import Nurse

'''
Contains common functions
'''

def access_hcno():
    '''
    get a health care number that may or may not be in the database already
    '''
    #get the health care number
    hcno = raw_input("Please enter patient hcno: ")

    # if the health care number is shorter than 5 digits or isn't 5 numbers
    while len(hcno) != 5 or hcno.isdigit() is False:
        print "Health care number is a 5 digit number"
        hcno = raw_input("Please enter patient hcno: ")
    return hcno

def get_symptom():
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    print "Now we need the symptom. For ease, you may enter one from this list or enter your own:"
    c.execute('''SELECT DISTINCT symptom FROM symptoms;''')
    resultat = c.fetchall()
    result = [str(x).strip("(u',)") for x in resultat] #get rid of the annoying formatting they seem to come with
    result.append("Custom") #add the option to add a custom symptom to the database

    # generate the numbers in the (x) part of the output
    for i in range(1, len(result)+1):
        x = result[i-1]
        print "(" + str(i) + ")  " + str(x)  
    
    answer = raw_input("Please enter your selection: ")
    while answer not in [str(i) for i in range(1, len(result)+1)]:
        print "Please enter an option from the list"
        answer = raw_input("Please enter your selection:")
    
    #map their answer to the entries in result
    symptom = result[int(answer)-1]
    
    #if they choose custom
    if answer == str(len(result)):
        #gets the low and high range of the age group and then concatenates them
        symptom = raw_input("Please enter the observed symptom: ")
        while len(symptom) > 15:
            print "Symptom must be shorter than 16 characters"
            symptom = raw_input("Please enter the observed symptom: ")
    return symptom 


def get_hcno():
    '''
    get a health care number that is definitely not in the database already
    '''
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    hcno = raw_input("Please enter the patient's health care number: ")

    #is that hcno in the database?
    c.execute('''SELECT * FROM patients WHERE hcno=? ''', (hcno, ))
    result = c.fetchone()

    while len(hcno) != 5 or hcno.isdigit() is False or result == None:
        if len(hcno) != 5 or hcno.isdigit() is False:
            print "Health Care Number must be exactly 5 digits"
        elif result == None:
            print "Health Care Number not in system"
        hcno = raw_input("Please enter the patient's health care number: ")
        c.execute('''SELECT * FROM patients WHERE hcno=? ''', (hcno, ))
        result = c.fetchone()
    return hcno

def get_name():
    '''
    get the patient's name in a format that doesn't violate any database constrictions
    '''
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    name = raw_input("Please enter the patient's name: ")

    while len(name) > 15 or name.replace(' ', '').isalpha() is False or len(name.replace(' ', '')) == 0:

        #name is too long
        if len(name) > 15: print "Name must be 15 characters or shorter."

        if name.replace(' ', '').isalpha() is False and len(name.replace(' ', '')) != 0:    #name contains numbers and is not blank
            print "Name must not contain numbers"          #when I left the blank check out, it popped up when this was empty

        #name contains entirely spaces
        if len(name.replace(' ', '')) == 0:  print "Name can't be blank"

        name = raw_input("Please enter the patient's name: ")

    return name.title() #capitalize first letter of each word and lowercase the rest

def get_age_group():
    '''
    get the age_group of the user in a format that fits the database schema
    '''
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    #get age group
    print "Now we need the age group. To make it homogeneous with the others we have"

    #find all the current age groups in the database
    c.execute('''
    SELECT DISTINCT age_group FROM patients ORDER BY age_group ;
    ''')
    resultat = c.fetchall()
    result = [str(x).strip("(u',)") for x in resultat] #get rid of the annoying formatting they seem to come with
    result.append("Custom") #add the option to add an age group to the database

    # generate the numbers in the (x) part of the output
    for i in range(1, len(result)+1):
        x = result[i-1]
        print "(" + str(i) + ")  " + str(x)

    answer = raw_input("Enter your selection: ") #still to add: make sure you got a number in the list, and that it's a number
    while answer not in [str(i) for i in range(1, len(result)+1)]:
        print "Please enter an option from the list"
        answer = raw_input("Enter your selection: ")

    #if they didn't choose custom
    age_group = result[int(answer)-1]

    #if they choose custom
    if answer == str(len(result)):
        exit = False
        while exit == False:
            #gets the low and high range of the age group and then concatenates them
            age_group_low = raw_input("Enter the lowest age in the group: ")
            age_group_hi = raw_input("Enter the highest age in the group: ")
            age_group = str(age_group_low).zfill(2) + '-' + str(age_group_hi).zfill(2) #zfill(2) enter 3 and it becomes 03, 8 becomes 08 and 10 remains 10
            test = raw_input("Add age group to db (y/n/exit)? : ")
            if test.lower().replace(' ', '') == 'exit':
                exit = True
            elif test.lower().replace(' ','') == 'y':
                exit = True
    return age_group

def get_address():
    '''
    get address in a format that works for the database schema
    '''

    address = raw_input("Please enter their address: ")
    while len(address)>30:
        print "address must be shorter than 31 characters"
        address = raw_input("Please enter their address: ")
    return address

def get_phone():
    '''
    gets the phone number of the patient in a format that fits the database schema
    '''
    phone = raw_input("Please enter phone number, format: 00000000000: ")
    while phone.isdigit() is False or len(phone) > 10:
        if phone.isdigit() is False:
            print "Please enter only digits"
        if len(phone) > 10:
            print "Please limit to 10 digits"

        phone = raw_input("Please enter phone number, format: 00000000000: ")
    return phone

def get_emg_phone(phone):
    '''
    gets the emergency phone number in a way that fits the database schema
    '''
    emg_phone = raw_input("Please enter emergency contact number.\n If it's the same as your phone number, just enter 's': ")
    if emg_phone.lower() == 's':
        emg_phone = phone
    while emg_phone.isdigit() is False:
        if emg_phone == 's':
            break
        print "Please enter only digits or 's'"
        emg_phone = raw_input("Please enter emergency contact number.\n If it's the same as your phone number, just enter 's': ")
        if emg_phone.lower() == 's':
            emg_phone = phone
    return emg_phone


def new_chart_ID():
    '''
    finds the first chart ID that is not currently in use, starting from 00001
    '''
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    for i in range(1, 100000):
        chart_id = str(i).zfill(5) #what zfill(5) does: 1 turns into 00001, 100 turns into 00100, 10000 and higher remain the same
        chart_id_format = (chart_id, )
        
        # is the chart ID already in use?
        c.execute('''SELECT * FROM charts WHERE chart_id=? ''', chart_id_format)
        result = c.fetchone()
        
        #if it isn't then break out of the loop and use that chart id
        if result == None:
            break
    return chart_id

def parse_file():
    '''
    takes the file path of an sql file within the same folder as hospital.py and executes all the commands found in the file.
    Don't use this for searching.. it's not for that.
    '''
    sql_file_path = raw_input("\nPlease enter the path of the sql document you would like to run or type 'exit': ")
    if sql_file_path.lower() == 'exit':
        return 0


    if sql_file_path is not '':
        while sql_file_path.replace(' ', '')[0] != '.':
            print "Format must be ./sql_document.sql"
            sql_file_path = raw_input("Please enter the path of the sql document you would like to run: ")

        conn = sqlite3.connect('./hospital.db')
        c = conn.cursor()
        try:
            with open(sql_file_path, 'r') as f:  #build the database structure
                lines = f.read()
            c.executemany(lines)
            # c.execute(lines.replace("'\n'", ''))
            conn.commit()
            result = c.fetchall()
            #for row in result:
                #print "hcno: ", row[0]
            print "Successfully ran file"
        except:
            print "There was an error processing your request"
    return 0

def Login_system():
    
    '''
    Handles logging in, passes control to Login() to get valid login information, which then returns the staff_id and role of who logged in. 
    Then it decides what to run based on the role receieved in the login process.
    '''
    while 0==0:
        staff_id, role = Login()
        if role == 'A':
            pass
            #Admin(staff_id)

        # Needs to be implemented as 'A' --> Admin(staff_ID) and ('D', 'N') ---> Care_Staff(role, staff_ID) as per the requirements
        elif role == 'D':
            pass
            #Doctor(staff_id)
        elif role == 'N':
            Nurse.Nurse(staff_id)
        elif role == 'S':
            return 'Shutdown'
        elif role == 0:
            return 0

def greeting():
    '''
    Just to clean up the code in hospital.py
    prompts the user to enter an option and returns that valid option
    '''
    prompt = "\nWhat would you like to do?\
            \n(1) Login\
            \n(2) Add data\
            \n(3) Shutdown\n: "
    answer = raw_input( prompt )
    while answer not in ['1', '2', '3']:
        answer = raw_input( prompt)
    return answer
