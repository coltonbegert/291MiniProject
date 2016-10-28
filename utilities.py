import sqlite3
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

def get_address():
    '''
    get address in a format that works for the database schema
    '''
    address = raw_input("Please enter their address: ")
    while len(address)>30:
        print "address must be shorter than 31 characters"
        address = raw_input("Please enter their address: ")
    return address

def get_Admin_diagnosis():
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    print "\nPlease select a diagnosis from this list:"

    # get every diagnosis that we've seen to date
    c.execute('''SELECT DISTINCT diagnosis FROM diagnoses ORDER BY diagnosis''')
    resultat = c.fetchall()
    result = [str(x).lstrip("(u'").rstrip("',)") for x in resultat] #get rid of the annoying formatting they seem to come with

    # generate the numbers in the (x) part of the output
    for i in range(1, len(result)+1):
        x = result[i-1]
        print "(" + str(i) + ")  " + str(x)

    answer = raw_input("Please enter your selection: ")
    #if the number entered is out of the range of our options, then keep asking for a correct answer
    while answer not in [str(i) for i in range(1, len(result)+1)]:
        print "Please enter an option from the list"
        answer = raw_input("Please enter your selection:")

    #map their answer to the entries in result
    diagnosis = result[int(answer)-1]
    return diagnosis    

def get_age_group():
    '''
    get the age_group of the user in a format that fits the database schema
    '''
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()

    #get age group
    print "Now we need the age group. To make it homogeneous with the others we have:"

    #find all the current age groups in the database
    c.execute('''SELECT DISTINCT age_group FROM dosage ORDER BY age_group;''')
    resultat = c.fetchall()
    result = [str(x).lstrip("(u'").rstrip("',)") for x in resultat] #get rid of the annoying formatting they seem to come with

    # generate the numbers in the (x) part of the output
    for i in range(1, len(result)+1):
        x = result[i-1]
        print "(" + str(i) + ")  " + str(x)


    answer = raw_input("Enter your selection: ")
    #if the number entered is out of the range of our options, then keep asking for a correct answer
    while answer not in [str(i) for i in range(1, len(result)+1)]:
        print "Please enter an option from the list"
        answer = raw_input("Enter your selection: ")

    age_group = result[int(answer)-1]
    return age_group

def get_diagnosis():
    '''
    gets the diagnosis in a way that works with the database
    '''
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    print "Now we need the diagnosis. For ease, you may enter one from this list or enter your own:"

    # get every diagnosis that we've seen to date
    c.execute('''SELECT DISTINCT diagnosis FROM diagnoses ORDER BY diagnosis''')
    resultat = c.fetchall()
    result = [str(x).lstrip("(u'").rstrip("',)") for x in resultat] #get rid of the annoying formatting they seem to come with
    result.append("Custom") #add the option to add a custom diagnosis to the database

    # generate the numbers in the (x) part of the output
    for i in range(1, len(result)+1):
        x = result[i-1]
        print "(" + str(i) + ")  " + str(x)

    answer = raw_input("Please enter your selection: ")
    #if the number entered is out of the range of our options, then keep asking for a correct answer
    while answer not in [str(i) for i in range(1, len(result)+1)]:
        print "Please enter an option from the list"
        answer = raw_input("Please enter your selection:")

    #map their answer to the entries in result
    diagnosis = result[int(answer)-1]

    #if they choose custom
    if answer == str(len(result)):
        diagnosis = raw_input("Please diagnose the patient: ")
        while len(diagnosis) > 20:
            print "Diagnosis must be shorter than 21 characters"
            diagnosis = raw_input("Please diagnose the patient: ")
    return diagnosis

def get_emg_phone(phone):
    '''
    gets the emergency phone number in a way that fits the database schema
    '''
    emg_phone = raw_input("Please enter emergency contact number.\nIf it's the same as your phone number, just enter 's': ")
    if emg_phone.lower() == 's':
        return phone

    #if they didn't enter all digits or if they tried to give us too long of a phone number
    while emg_phone.isdigit() is False or len(emg_phone) >10:

        print "\nPlease enter only 10 digits or 's'"
        emg_phone = raw_input("Please enter emergency contact number.\nIf it's the same as your phone number, just enter 's': ")
        if emg_phone.lower() == 's':
            return phone
    return emg_phone

def get_e_med_date():
    '''
    gets the ending date of a prescription in a format that works with the database
    '''
    end_med = raw_input("Please enter end date of medication in the following format: YYYY-MM-DD HH:MM:SS: ")
    em = end_med.lstrip(' ')
    while em[4] != '-' or em[7] != em[4] or em[13] != em[16] or em[13] != ':':
        end_med = raw_input("Please enter end date of medication in the following format: YYYY-MM-DD HH:MM:SS: ")
        em = end_med.lstrip(' ')
    return end_med

def get_hcno():
    '''
    get a health care number that is definitely in the database already
    '''
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    hcno = raw_input("Please enter the patient's health care number: ")

    #is that hcno in the database?
    c.execute('''SELECT * FROM patients WHERE hcno=? ''', (hcno, ))
    result = c.fetchone()

    #if the hcno isn't exactly 5 digits or isn't in the database, keep asking
    while len(hcno) != 5 or hcno.isdigit() is False or result == None:

        #specific messages for each type of error
        if len(hcno) != 5 or hcno.isdigit() is False:
            print "Health Care Number must be exactly 5 digits"
        elif result == None:
            print "Health Care Number not in system"

        #get the hcno again and recheck if it's in the db
        hcno = raw_input("Please enter the patient's health care number: ")
        c.execute('''SELECT * FROM patients WHERE hcno=? ''', (hcno, ))
        result = c.fetchone()

    return hcno

def get_medication():
    '''
    get the medication the doctor chooses to prescribe
    '''
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()

    #get medication
    print "Now we need the medication. Choose from following list:"

    #find all the current medications in the database
    c.execute('''SELECT DISTINCT drug_name FROM drugs ORDER BY drug_name''')

    resultat = c.fetchall()
    result = [str(x).lstrip("(u'").rstrip("',)") for x in resultat] #get rid of the annoying formatting they seem to come with

    # generate the numbers in the (x) part of the output
    for i in range(1, len(result)+1):
        x = result[i-1]
        print "(" + str(i) + ")  " + str(x)

    answer = raw_input("Enter your selection: ")

    #if the number entered is out of the range of our options, then keep asking for a correct answer
    while answer not in [str(i) for i in range(1, len(result)+1)]:
        print "Please enter an option from the list"
        answer = raw_input("Enter your selection: ")

    medication = result[int(answer)-1]
    return medication




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



def get_phone():
    '''
    gets the phone number of the patient in a format that fits the database schema
    '''
    phone = raw_input("Please enter phone number, format: 00000000000: ")

    #only allows length 10 phone numbers made up entirely of digits
    while phone.isdigit() is False or len(phone) != 10:
        if phone.isdigit() is False:
            print "Please enter only digits"
        if len(phone) != 10:
            print "Please enter exactly 10 digits"

        phone = raw_input("Please enter phone number, format: 00000000000: ")
    return phone

def get_symptom():
    '''
    gets the symptom in a format that works with the database
    '''
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()

    print "Now we need the symptom. For ease, you may enter one from this list or enter your own:"

    #list all the symptoms that have been seen so far
    c.execute('''SELECT DISTINCT symptom FROM symptoms ORDER BY symptom''')
    resultat = c.fetchall()
    result = [str(x).lstrip("(u'").rstrip("',)") for x in resultat] #get rid of the annoying formatting they seem to come with
    result.append("Custom") #add the option to add a custom symptom to the database

    # generate the numbers in the (x) part of the output
    for i in range(1, len(result)+1):
        x = result[i-1]
        print "(" + str(i) + ")  " + str(x)


    answer = raw_input("Please enter your selection: ")

    #while answer isn't one of the numbers offered, keep pestering until they enter a correct one
    while answer not in [str(i) for i in range(1, len(result)+1)]:
        print "Please enter an option from the list"
        answer = raw_input("Please enter your selection:")

    #map their answer to the entries in result
    symptom = result[int(answer)-1]

    #if they choose custom
    if answer == str(len(result)):
        symptom = raw_input("Please enter the observed symptom: ")
        while len(symptom) > 15:
            print "Symptom must be shorter than 16 characters"
            symptom = raw_input("Please enter the observed symptom: ")
    return symptom


def get_s_med_date(mdate):
    '''
    gets the starting date of a prescribed medication, if it's the same as the date it's being prescribed then user can enter 'S'
    '''

    start_med = raw_input("Enter start date of medication in the following format: YYYY-MM-DD HH:MM:SS, \nor enter S if start date is same as prescription date: ")
    sm = start_med.lstrip(' ')

    #checks that the format of YYYY-MM-DD HH:MM:SS is not violated if it's a date, or if it's 's', both are acceptable
    while sm.upper() != 'S' and (len(sm) < 17 or sm[4] != '-' or sm[7] != sm[4] or sm[13] != sm[16] or sm[13] != ':'):
        start_med = raw_input("Please enter start date of medication in the following format: YYYY-MM-DD HH:MM:SS, \nor enter S if start date is same as prescription date: ")
        sm = start_med.lstrip(' ')
    if sm.upper() == 'S':
        start_med = mdate
    return start_med


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

        #if it isn't then return that unused chart ID
        if result == None:
            return chart_id


def parse_file():
    '''
    takes the file path of an sql file within the same folder as hospital.py and executes all the commands found in the file.
    Don't use this for searching.. it's not for that.
    '''
    sql_file_path = raw_input("\nPlease enter the path of the sql document you would like to run or type 'exit': ")
    if sql_file_path.lower() == 'exit':
        return 0

    #it is not blank
    if sql_file_path is not '':
        #if the first two characters (with all spaces removed) are './' then most likely the format is correct
        while sql_file_path.replace(' ', '')[0] != '.' or sql_file_path.replace(' ', '')[1] != '/':
            print "Format must be ./sql_document.sql"
            sql_file_path = raw_input("Please enter the path of the sql document you would like to run: ")

        conn = sqlite3.connect('./hospital.db')
        c = conn.cursor()

        try:
            with open(sql_file_path, 'r') as f:  #open the file and read all the lines
                lines = f.read()
            c.executescript(lines) #execute all the lines in the file
            conn.commit()        #commit the changes
            print "Successfully ran file"
        except:
            print "There was an error processing your request"
    return 0