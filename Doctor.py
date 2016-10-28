import sqlite3
from time import gmtime, strftime
import utilities
import Nurse

def Doctor(sid, role):
    while 0==0:
        print"option 2, 3 and 5 work for now"
        answer = raw_input("What option would you like to choose?\n\
        (1) Display Chart information for a patient\n\
        (2) Record a symptom\n\
        (3) Record a diagnosis\n\
        (4) Prescribe a medication\n\
        (5) Logout user\n\
        \nSelection: ")
        if answer == '1': 
            Display_Charts()
        
        if answer == '2': 
            Record_Symptom(sid, role)
        
        if answer == '3': 
            Add_Diagnosis(sid)
        
        if answer == '4': 
            Add_Medication(sid)
        
        if answer == '5':
            print '\nLogging out'
            return 0



#not yet implemented
def Display_Charts():
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    
    #get the health care number
    hcno = utilities.get_hcno()
    #get their name and use it in a prompt
    c.execute('''select name from patients where hcno=?''', (hcno,))
    name = str(c.fetchone()).lstrip("(u'").rstrip("',)")
    print "Here are all the charts for", name +':'
    
    #get info associated with the hcno, in chronological order
    print "not implemented"
    return 0

#    c.execute(''' SELECT * FROM charts c WHERE c.hcno = ? Select * FROM symptoms s where s.hcno=? order by obs_date UNION select * From diagnoses d where d.hcno=? order by ddate UNION select * from medications m where m.hcno = ? order by ddate''', (hcno,hcno, hcno, hcno)) #THIS IS NOT CORRECT
    
    #charts = c.fetchall()
    #charts = [str(x).lstrip("(u'").rstrip("',)") for x in charts] #fix the formatting
    
    ## choose the chart
    #chart_id = raw_input("Enter the chartID you wish to look up")
    
    ## gather all entries from selected chart 
    
    #c.execute(''' Select * FROM symptoms order by obs_date group by hcno UNION select * From diagnoses order by ddate group by hcno UNION select * from medications order by ddate group by hcno;''')

def Record_Symptom(staff_id, role):
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    hcno = utilities.get_hcno()
    c.execute(''' select chart_ID from charts where hcno=? AND edate is Null;''', (hcno,))
    result = c.fetchone()
    if result == None:
        print "No open chart for given Health Care Number"
        if role == 'N':
            answer = raw_input("Would you like to open a chart for this patient?(y/n): ")
            if answer.lower() == 'y':
                Nurse.Create_Chart_Add_Patient(hcno)
            elif answer.lower() == 'n':
                print "No chart created and no symptom recorded"
                return 0
            
            answer = raw_input("Continue adding symptom for patient?(y/n): ")
            if answer.lower() == 'n':
                return 0
            c.execute(''' select chart_ID from charts where hcno=? AND edate is Null;''', (hcno,))
            result = c.fetchone()
            chart_id = str(result).lstrip("(u'").rstrip("',)")
            
        else:
            return 'fatal'
    else:
        chart_id = str(result).lstrip("(u'").rstrip("',)")
    symptom = utilities.get_symptom()
    obs_date = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #current time
    insertion = [(hcno, chart_id, staff_id, obs_date, symptom)]
    try:
        c.executemany(''' INSERT into symptoms VALUES (?,?,?,?,?)''', insertion)
        conn.commit()
        print "Entry added"
    except:
        print "There was an error processing your request"




def Add_Diagnosis(staff_id):
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    hcno = utilities.get_hcno()
    c.execute(''' select chart_ID from charts where hcno=? AND edate is Null;''', (hcno,))
    result = c.fetchone()
    if result == None:
        print "No open chart for given Health Care Number"
        return 'fatal'
    else:
        chart_id = str(result).lstrip("(u'").rstrip("',)")
    diagnosis = utilities.get_diagnosis()
    ddate = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #current time
    insertion = [(hcno, chart_id, staff_id, ddate, diagnosis)]
    try:
        c.executemany(''' INSERT into diagnoses VALUES (?,?,?,?,?)''', insertion)
        conn.commit()
        print "Entry added"
    except:
        print "There was an error processing your request"


def Add_Medication(staff_id):
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    
    # get the health care number
    hcno = utilities.get_hcno()    
    c.execute(''' select chart_ID from charts where hcno=? AND edate is Null;''', (hcno,))
    result = c.fetchone()
    if result == None:
        print "\nNo open chart for given Health Care Number"
        return 'fatal'
    else:
        chart_id = str(result).lstrip("(u'").rstrip("',)") 
    
    c.execute(''' select distinct symptom from symptoms where chart_id = ?''', (chart_id,))
    result = c.fetchall()
    if result != None:
        print result
        for entry in result:
            print entry[0]
        
    c.execute(''' select name from patients where hcno=? ''', (hcno,))
    name = str(c.fetchone()).lstrip("(u'").rstrip("',)") 
        
    print "Fetched open chart with chart ID", chart_id, "\nPatient name:", name
    
    medication = utilities.get_medication()
    mdate = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #current time
    
    start_med_date = utilities.get_s_med_date(mdate)
    end_med_date = utilities.get_e_med_date()
    amount = raw_input("\nPlease enter the amount of medication you wish to prescribe: ")
    
    #lookup suggested dose of specific medication for age range of the patient
    c.execute('''select sug_amount from dosage d, patients p where p.hcno=:hcno AND d.age_group = p.age_group AND drug_name=:med''', {'med':medication, 'hcno':hcno})
    sug_amount = str(c.fetchone()).lstrip("(u'").rstrip("',)")
    
    #and get their age group
    c.execute('''SELECT age_group from patients where hcno=?''', (hcno,))
    age_group = str(c.fetchone()).lstrip("(u'").rstrip("',)")
    
    while int(amount) > int(sug_amount):
        print "\nWarning, this patient is in the age group", age_group, "and the suggested dose of", medication, "for that age group is", sug_amount + '.'
        answer = raw_input("Do you wish to continue(y/n/exit): ")
        if answer.lower() == 'exit':
            return 'early end'
        if answer.lower() == 'y':
            break
        else:
            amount = raw_input("Please enter the amount of medication you wish to prescribe or type exit: ")
            if amount.lower() == 'exit':
                return 'early end'
        
    
    return 0
        
    
    
    
    
    
        
        
        
        
        
    insertion = [(hcno, chart_id, staff_id, mdate, medication)]
    print insertion
    try:
        c.executemany(''' INSERT into diagnoses VALUES (?,?,?,?,?)''', insertion)
        conn.commit()
        print "Entry added"
    except:
        print "There was an error processing your request"    
    
    
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
    