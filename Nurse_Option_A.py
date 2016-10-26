import sqlite3
from time import gmtime, strftime
#from utilities import get_name, get_age_group, get_address, access_hcno, get_emg_phone, get_phone
import utilities

def Nurse_Option_A(hcno = None):
    #connect to the database
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    
    #checks if the optional argument is blank or not
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