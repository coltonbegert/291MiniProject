import sqlite3
from time import gmtime, strftime
import utilities

#       Rough Draft
#       Needs Work
#     
#
#



def Doctor_Option_A():
    conn = sqlite.connect("./hospital.db")
    c = conn.cursor()
    
    #get the health care number
    hcno = raw_input("Enter patient's hcno: ")
    
    if len(hcno) != 5 or hcno.isdigit() is False:
            print ("Health care number is a 5 digit number")
            hcno = raw_input("Please enter patient hcno: ")    

    # figure out if the hcno is already in the database    
    c.execute('''SELECT * FROM patients WHERE hcno=? ''', (hcno, ))
    result = c.fetchone()
        
    if result == None:
        print ("Oops, patient not in database.")
        return
    
    # get all charts in system
    
    c.execute(''' SELECT * FROM charts c, where c.hcno = result order by c.adate''')
    
    # choose the chart
    chartid = raw_input("Enter the chartID you wish to look up")
    
    # gather all entries from selected chart 
    
    c.execute(''' Select * FROM symptoms order by obs_date group by hcno UNION select * From diagnoses order by ddate group by hcno UNION select * from medications order by ddate group by hcno;''')

def Doctor_Option_B(staff_id):
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    hcno = utilities.get_hcno()
    c.execute(''' select chart_ID from charts where hcno=? AND edate is Null;''', (hcno,))
    result = c.fetchone()
    print result
    if result == None:
        print "No open chart for given Health Care Number"
        return 'fatal'
    else:
        chart_id = str(result).strip("(,)u'")
    symptom = utilities.get_symptom()
    obs_date = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #current time
    insertion = [(hcno, chart_id, staff_id, obs_date, symptom)]
    print insertion
    try:
        c.executemany(''' INSERT into symptoms VALUES (?,?,?,?,?)''', insertion)
        conn.commit()
        print "Entry added"
    except:
        print "There was an error processing your request"




def Doctor_Option_C(staff_id):
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    hcno = utilities.get_hcno()
    c.execute(''' select chart_ID from charts where hcno=? AND edate is Null;''', (hcno,))
    result = c.fetchone()
    print result
    if result == None:
        print "No open chart for given Health Care Number"
        return 'fatal'
    else:
        chart_id = str(result).strip("(,)u'")
    diagnosis = utilities.get_diagnosis()
    ddate = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #current time
    insertion = [(hcno, chart_id, staff_id, ddate, diagnosis)]
    print insertion
    try:
        c.executemany(''' INSERT into diagnoses VALUES (?,?,?,?,?)''', insertion)
        conn.commit()
        print "Entry added"
    except:
        print "There was an error processing your request"


def Doctor_Option_D():
    conn = sqlite.connect("./hospital.db")
    c = conn.cursor()

    # get the health care number
    hcno = raw_input("Enter patient's hcno: ")

    if len(hcno) != 5 or hcno.isdigit() is False:
        print ("Health care number is a 5 digit number")
        hcno = raw_input("Please enter patient hcno: ")

        # figure out if the hcno is already in the database
    c.execute('''SELECT * FROM patients WHERE hcno=? ''', (hcno,))
    result = c.fetchone()


    if result == None:
        print ("Oops, patient not in database.")

    # show all open charts for patient

    c.execute(''' Select chart_id from charts where edate is NULL and hcno = ?''', (result,))
    result = c.fetchall()

    
    
    #Additional Checks


    c.execute('Select amount from medications where hcno = hcno  ', {'hcno',result})

    prescribedAmount = c.fetchall

    c.execute(''' Select sug_amount from dosage where age_group = age;''')
    recomendedAmount = c.fetchall


    
    if (prescribedAmount > recomendedAmount):
        print("WARNING")

    
    print("Would you like to Change perscription")
    change= raw_input("Enter Yes or NO") 
    
    if (change == 'Yes'):
        # change perscription
        print("flag")
    
    # get allergy data
    
    c.execute(''' select drug_name from reportedallergies where hcno = hcno''')

    print("WARNING")
    print("Patient is allergic to " + drugName)
    
    # get possible allergies 
    c.execute(''' SELECT canbe_alg from inferredallergies where alg = drugName;''')
    
    print("Patient may be allegic to " + inferedAllergy + " inferred from" + drugName) 


    mdate = strftime("%A, %d %B %Y %H:%M:%S", gmtime())

    # pass staff_id

    start_med = raw_input("Enter start date")
    end_med = raw_input("Enter end date")
    amount = raw_input("Enter amount")
    drug_name = raw_input("Enter drug_name")

    c.execute(''' Insert Into medications (hcno, chart_id, staff_id, mdate, start_med, end_med, amount, drug_name ''')
    