import sqlite3
from Nurse_Option_A import Nurse_Option_A
from time import gmtime, strftime

def Nurse_Option_B():
    '''
    Allows a Nurse to close a patient's most recently opened chart
    Note, this calls Nurse_Option_A in order to open a new chart if desired
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
    c.execute('SELECT chart_id FROM charts WHERE hcno=:hcno AND edate=:edate ORDER BY adate DESC', {'hcno':hcno, 'edate':'Null'})
    chart_id = str(c.fetchone()).strip("(u',)")

    if chart_id == str(None):
        print "No open chart found for this patient"
        answer = raw_input("Would you like to open one(y/n)?: ")
        if answer.lower() == 'y':
            return Nurse_Option_A(hcno)
        print "No new chart created"
        return 0
        
    else:
        print "Found chart with chart ID:", chart_id
        answer = raw_input("Would you like to close this chart (y/n)?: ")
        if answer.lower() == 'y':
            edate = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            c.execute('UPDATE charts SET edate=:edate WHERE chart_id=:chart_id', {'edate':edate, 'chart_id':chart_id} ) 
            conn.commit()
            print "Chart updated"
        else:
            print "Chart remains open"
