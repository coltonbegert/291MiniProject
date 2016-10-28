import sqlite3
from time import gmtime, strftime
import utilities
import Nurse

def Doctor(sid, role):
    while 0==0:
        answer = raw_input("What option would you like to choose?\n\
        (1) Display Chart information for a patient\n\
        (2) Record a symptom\n\
        (3) Record a diagnosis\n\
        (4) Prescribe a medication\n\
        (5) Logout user\n\
        \nSelection: ")
        if answer == '1':
            Display_Charts()

        elif answer == '2':
            Record_Symptom(sid, role)

        elif answer == '3':
            Add_Diagnosis(sid)

        elif answer == '4':
            Add_Medication(sid)

        elif answer == '5':
            print '\nLogging out'
            return 0
        else:
            print "\nInvalid option\n"




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

    # c.execute(''' select chart_id, adate from (Select chart_id || ' is closed' as chart_id , adate as adate From charts where hcno = ? and edate is not Null UNION Select chart_id || 'is open' as chart_id, adate as adate From charts where hcno = ? and edate is Null) order by adate asc;''',(hcno,hcno))
    c.execute('''SELECT c.chart_id, c.adate, c.edate, CASE WHEN (c.edate is NULL) THEN 'Open' ELSE 'Closed' END status
    FROM charts c
    WHERE c.hcno = ?
    ORDER BY c.adate ASC;''', ([hcno]))

    charts = c.fetchall()


    # for row in charts:
    #     print row[0]


    print "Choose Chart:"

    for i in range(len(charts)):
        print "\t(%d) Chart: %s with Status: %s " %(i+1, charts[i][0], charts[i][3])
    print ("\t(%d) Cancel" %(len(charts)+1))



    chart_id = eval(raw_input ("Choose Chart ID: ")) -1
    if (chart_id != len(charts)):
        # chart_id = raw_input("Which Chart would you to look at: ")
        chart_id = str(charts[chart_id][0])
        c.execute('''SELECT type, cdate, value, name
        FROM (
          SELECT 'Symptom' as type, s.obs_date as cdate, s.symptom as value, st.name as name
          FROM charts c, symptoms s, staff st
          WHERE c.chart_id = s.chart_id
          AND c.chart_id = (?)
          AND st.staff_id = s.staff_id
          UNION
          SELECT 'Diagnosis' as type, d.ddate as cdate, d.diagnosis as value, s.name as name
          FROM charts c, diagnoses d, staff s
          WHERE c.chart_id = d.chart_id
          AND c.chart_id = (?)
          AND s.staff_id = d.staff_id
          UNION
          SELECT 'Medication' as type, m.mdate as cdate, m.drug_name as value, s.name as name
          FROM charts c, medications m, staff s
          WHERE c.chart_id = m.chart_id
          AND c.chart_id = (?)
          AND s.staff_id = m.staff_id
        )
        ORDER BY cdate ASC;''', ([chart_id, chart_id, chart_id]))

        data = c.fetchall()
        # print "Hello"
        for row in data:
            # print data
            print "\tA %s, %s, was recorded on %s by %s" %(row[0], row[2], row[1], row[3])
        print
        return 1

    else:
        return 0

#    c.execute(''' SELECT * FROM charts c WHERE c.hcno = ? Select * FROM symptoms s where s.hcno=? order by obs_date UNION select * From diagnoses d where d.hcno=? order by ddate UNION select * from medications m where m.hcno = ? order by ddate''', (hcno,hcno, hcno, hcno)) #THIS IS NOT CORRECT

    #charts = c.fetchall()
    #charts = [str(x).lstrip("(u'").rstrip("',)") for x in charts] #fix the formatting

    ## choose the chart
    #chart_id = raw_input("Enter the chartID you wish to look up")

    ## gather all entries from selected chart

    #c.execute(''' Select * FROM symptoms order by obs_date group by hcno UNION select * From diagnoses order by ddate group by hcno UNION select * from medications order by ddate group by hcno;''')

def Record_Symptom(staff_id, role):
    #connect to the DB
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    #get the hcno of a patient that exists in the db
    hcno = utilities.get_hcno()

    #does that patient have an open chart?
    c.execute(''' select chart_id from charts where hcno=? AND edate is Null;''', (hcno,))
    result = c.fetchone()

    # if they have no open chart take this path, otherwise go right to entering the symptom
    # this allows only a nurse to take the first nurse option, which is to open a chart and then continue along the process
    # of adding a patient, while a doctor is not allowed to open a new chart
    if result == None:
        print "No open chart for given Health Care Number"
        if role == 'N':
            answer = raw_input("Would you like to open a chart for this patient?(y/n): ")

            #opens a new chart for this patient
            if answer.lower() == 'y':
                Nurse.Create_Chart_Add_Patient(hcno)

            #exits to action screen
            elif answer.lower() == 'n':
                print "No chart created and no symptom recorded"
                return 0

            answer = raw_input("Continue adding symptom for patient?(y/n): ")
            #exits to action screen
            if answer.lower() == 'n':
                return 0

            #get the chart ID of the newly opened chart
            c.execute(''' select chart_id from charts where hcno=? AND edate is Null;''', (hcno,))
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
    c.execute(''' select chart_id from charts where hcno=? AND edate is Null;''', (hcno,))
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
    c.execute(''' select chart_id from charts where hcno=? AND edate is Null;''', (hcno,))
    result = c.fetchone()
    if result == None:
        print "\nNo open chart for given Health Care Number"
        return 'fatal'
    else:
        chart_id = str(result).lstrip("(u'").rstrip("',)")

    c.execute(''' select name from patients where hcno=? ''', (hcno,))
    name = str(c.fetchone()).lstrip("(u'").rstrip("',)")

    print "\nFetched open chart with chart ID", chart_id, "\nPatient name:", name

    c.execute(''' select distinct symptom from symptoms where chart_id = ?''', (chart_id,))
    result = c.fetchall()
    if result != []:
        print "\nCurrently reported symptoms are as follows:"
        for entry in result:
            print entry[0]
        print '\n'
    else:
        print "\nNo symptoms currently related to this chart\n"

    medication = allergy_check(hcno)
    if medication == 'exit':
        return 0
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


    mdate = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #current time

    start_med_date = utilities.get_s_med_date(mdate)
    end_med_date = utilities.get_e_med_date()
    insertion = [(hcno, chart_id, staff_id, mdate, start_med_date, end_med_date, amount, medication)]

    try:
        c.executemany(''' INSERT into medications VALUES (?,?,?,?,?,?,?,?)''', insertion)
        conn.commit()
        print "Entry added"
    except:
        print "There was an error processing your request"


def allergy_check(hcno):
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    medication = utilities.get_medication()
    c.execute('''Select drug_name from reportedallergies where hcno=? and drug_name=?''', (hcno, medication))
    reportedallergies = c.fetchone()
    c.execute('''SELECT canbe_alg FROM reportedallergies r, inferredallergies i WHERE r.drug_name = i.alg and r.hcno=? and i.canbe_alg=?''', (hcno,medication))
    canbe_alg = c.fetchone()

    if reportedallergies != None:
        print "Patient has reported an allergy to", medication
        answer = raw_input("Would you like to change the drug prescription? (y/n/exit): ")
        if answer.lower() == 'y':
            return allergy_check(hcno)
        elif answer.lower() == 'exit':
            return 'exit'

    elif canbe_alg != None:
        allergy = str(canbe_alg).lstrip("(u'").rstrip("',)")
        print "Patient has a possible allergy to", allergy
        answer = raw_input("Would you like to change the drug prescription? (y/n/exit): ")
        if answer.lower() == 'y':
            return allergy_check(hcno)
        elif answer.lower() == 'exit':
            return 'exit'

    return medication

# role = 'D'
# Doctor(14434, role)
