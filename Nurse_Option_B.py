import sqlite3
from Nurse_Option_A import Nurse_Option_A
from time import gmtime, strftime
import utilities

def Nurse_Option_B():
    '''
    Allows a Nurse to close a patient's most recently opened chart
    Note, this calls Nurse_Option_A in order to open a new chart if desired
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
        #take the user to a special case of Nurse_Option_A, if hcno is supplied, it immediately tries to open a new chart for that hcno if there isn't already one that's open
        if answer.lower() == 'y':
            return Nurse_Option_A(hcno)
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
