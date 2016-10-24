import sqlite3
from time import gmtime, strftime

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
    
def Doctor_Option_C():
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
    
    # show all open charts for patient
    
    c.execute(''' Select * from charts where hcno = result''')
    
    chartid = raw_input("Enter the chartID you wish to look up")
    
    # get diagnosis 
    
    diagnosis = raw_input("Please enter the diagnosis")
    while len(diagnosis) > 20:
        print ("diagnosis must be shorted than 21 characters")
        diagnosis = raw_input ("Please enter their address:")
    
    # get date
       
    ddate = strftime("%A, %d %B %Y %H:%M:%S", gmtime())
    
    # staff_id = staff_id
    
    c.execute(''' INSERT into diagnoses values ( result, chart_id, staff_id, ddate, diagnosis); ''')
    

def Doctor_Option_D():
    
    # same code
    
    
    #Additional Checks 
    
    if (prescribedAmount > recomendedAmount):
        print("WARNING")
        c.execute(''' Select sug_amount from dosage where age_group = age;''')
    
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
    
    