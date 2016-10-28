import sqlite3
from time import gmtime, strftime
import Doctor
import utilities


def Nurse(role, sid):
    while 0==0:
        print"option 1, 2 and 5 work for now"
        answer = raw_input("What option would you like to choose?\n\
        (1) Create a new chart/add a patient\n\
        (2) Close a patient's chart\n\
        (3) Display Chart information for a patient\n\
        (4) Record a symptom\n\
        (5) Logout user\n\
        \nSelection: ")
        if answer == '1': 
            Create_Chart_Add_Patient()
        
        if answer == '2': 
            Close_Chart()
        
        if answer == '3': 
            Doctor.Display_Charts(sid)
        
        if answer == '4': 
            Doctor.Record_Symptom(sid, role)
        
        if answer == '5':
            print '\nLogging out'
            return 0

def Create_Chart_Add_Patient(hcno = None):
    #connect to the database
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    
    #checks if the optional argument is blank or not, if it has a hcno provided, it moves straight to checking if there's an open chart
    if hcno == None:
        #prompts user for health care number
        hcno = utilities.access_hcno()
        
        # figure out if the hcno is already in the database    
        c.execute('''SELECT * FROM patients WHERE hcno=? ''', (hcno, ))
        result = c.fetchone()
        
        #if not then
        if result == None:
            print "Oops, patient not in database."
            answer = raw_input("Would you like to enter patient into database(y/n)?: ")
            
            while answer.lower() not in ['y', 'n']:
                answer = raw_input("Would you like to enter patient into database(y/n)?: ")
                
            if answer.lower() == 'n':
                Nurse_Option_A() #start the process over again
                return 0
                
            if answer.lower() == 'y':
                name = utilities.get_name()
                age_group = utilities.get_age_group()
                address = utilities.get_address()
                phone = utilities.get_phone()
                emg_phone = utilities.get_emg_phone(phone)
                insertion = [(hcno, name, age_group, address, phone, emg_phone)]
                c.executemany('INSERT INTO patients VALUES (?,?,?,?,?,?)', insertion)
                conn.commit()
            

    #any charts open for that hcno?
    c.execute('SELECT chart_id FROM charts WHERE hcno=:hcno AND edate is Null ORDER BY adate DESC', {'hcno':hcno})
    chart_id = str(c.fetchone()).strip("(u',)")
    
    # if there are: allow them to leave it open or close it and make a new one
    if chart_id != str(None):
        print "Found chart with chart id", chart_id
        question = raw_input("Would you like to close this chart and open a new one(Y/N)?: ")
        
        if question.upper() == 'Y':
            edate = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #current time
            #update that chart to have the edate as the current time
            c.execute('UPDATE charts SET edate=:edate WHERE chart_id=:chart_id', {'edate':edate, 'chart_id':chart_id} )
            conn.commit()
            
        else:
            print "The chart stays open"
            return 0
            
        
    #selects the first unused chart number from 00001 to 99999
    chart_id = utilities.new_chart_ID()
    
    adate = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #current time
    insertion = [(chart_id, hcno, adate, None)]
    
    try:
        c.executemany('INSERT INTO charts VALUES (?,?,?,?)', insertion) #inserts our newly opened chart into the charts table
        conn.commit()
        print "\nCreated new chart for patient with following information:"
        print "----------------------------------------------------------"
        print "Chart ID:           ", chart_id
        print "Health Care Number: ", hcno
        print "Date Opened:        ", strftime("%A, %d %B %Y %H:%M:%S", gmtime())
        print "----------------------------------------------------------"
        return 0
    except:
        print "Something went wrong while storing or printing the chart information"
        return -1    

def Close_Chart():
    '''
    Allows a Nurse to close a patient's most recently opened chart
    Note, this calls Create_Chart_Add_Patient in order to open a new chart if desired
    '''
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    #gets the hcno from the user
    hcno = utilities.get_hcno()
    
    #are there any open charts for this hcno?
    c.execute('SELECT chart_id FROM charts WHERE hcno=:hcno AND edate is Null ORDER BY adate DESC', {'hcno':hcno})
    chart_id = str(c.fetchone()).strip("(u',)")
    
    #if there are no open charts:
    if chart_id == str(None):
        print "No open chart found for this patient"
        answer = raw_input("Would you like to open one(y/n)?: ")
        #take the user to a special case of Create_Chart_Add_Patient, if hcno is supplied, it immediately tries to open a new chart for that hcno if there isn't already one that's open, which there isn't
        if answer.lower() == 'y':
            return Create_Chart_Add_Patient(hcno)
        print "No new chart created"
        return 0
    
    #There is already an open chart:
    else:
        print "Found chart with chart ID:", chart_id
        answer = raw_input("Would you like to close this chart (y/n)?: ")
        if answer.lower() == 'y':
            edate = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #current time
            #closes currently open chart
            c.execute('UPDATE charts SET edate=:edate WHERE chart_id=:chart_id', {'edate':edate, 'chart_id':chart_id} ) 
            conn.commit()
            print "Chart", chart_id, "closed on date", edate
        else:
            print "Chart remains open"
