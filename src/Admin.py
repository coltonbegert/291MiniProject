import sqlite3
import utilities

def Admin():
    # Present the options for admin staff and loop for valid response
    while 0==0:
        option = raw_input("What would you like to do?\n\t(1) Report drugs prescribed by Doctors\n\t(2) Prescribing information for drug categories\n\t(3) Medication recommendations for for diagnoses\n\t(4) Search for drug applications\n\t(5) Logout\n:")
        if option == '1':
            drug_prescribed()
        elif option == '2':
            prescribed_drugs()
        elif option == '3':
            med_recommend()
        elif option == '4':
            drug_uses()
        elif option == '5':
            return 0
        else:
            print "\nInvalid option\n"
# connects to the sql databse
def connect_db(db_name = "./hospital.db"):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    return conn, c
# disconecnts for the sql database
def disconnect_db(conn):
    conn.commit()
    conn.close()
    return
# the first option for admin creates a report of the amount of each drug prescribed over a time period
# The amount is the amount per day x the number of days taking the drug
def drug_prescribed():
    print "\nDefine time period"
    
    #get a correctly formatted date
    start_date = raw_input("Enter start of time period (YYYY-MM-DD): ")
    sd = start_date.lstrip(' ')
    while sd[4] != '-' or sd[7] != sd[4] or len(sd) != 10:
        print "Please enter a date in a valid form"
        start_date = raw_input("Enter start of time period (YYYY-MM-DD): ")
        sd = start_date.lstrip(' ')
    start_date = sd
    
    #get a correctly formatted date
    end_date = raw_input("\nEnter end of time period (YYYY-MM-DD): ")
    ed = end_date.lstrip(' ')
    while ed[4] != '-' or ed[7] != ed[4] or len(ed) != 10:
        print "Please enter a date in a valid form"
        end_date = raw_input("Enter end of time period (YYYY-MM-DD): ")
        ed = end_date.lstrip(' ')    
    end_date = ed
    
    conn, c = connect_db()

# SQL statement for pulling the amount and name of each drug that a doctor prescribes over a time period.
# Assumptions: reolution of 1 day, amount = daily dose x number of days prescribed,
#              amount is the total amount even if perion is larger than specified time period
# grouped by the doctors name
    c.execute('''SELECT s.name, m.drug_name, sum(m.amount* (cast(julianday(m.end_med) as int) - cast(julianday(m.start_med) as int)))
        FROM staff s, medications m
        WHERE m.staff_id = s.staff_id
        AND m.mdate between date(?) and  date(?)
        GROUP BY s.name, m.drug_name
        HAVING s.role = 'D'
        ORDER BY s.name;''', (start_date,end_date))


    result = c.fetchall()
    
    if result == []:
        print "\nNo drugs found for that time period\n"
        return 0
    
    # uses the values returned form the sql statement
    # only prints doctors name once and indents all drugs and the total amount of all medication prescribed in range    
    print "\nAmount of each drug prescribed by each doctor in that time period:"
    last_name = ""
    for row in result:
        if row[0] != last_name:
            print row[0]
        last_name = row[0]
        print "\t",row[1],row[2]



# closes db connection
    print
    disconnect_db(conn)


# Second option for admin, makes a report of the amount of each drug prescribed in a time period

def prescribed_drugs():
    conn,c = connect_db()
# gets user input for date range
    print "\nDefine time period"
    
    #get a correctly formatted date
    start_date = raw_input("Enter start of time period (YYYY-MM-DD): ")
    sd = start_date.lstrip(' ')
    while sd[4] != '-' or sd[7] != sd[4] or len(sd) != 10:
        print "Please enter a date in a valid form"
        start_date = raw_input("Enter start of time period (YYYY-MM-DD): ")
        sd = start_date.lstrip(' ')
    start_date = sd
    
    #get a correctly formatted date
    end_date = raw_input("\nEnter end of time period (YYYY-MM-DD): ")
    ed = end_date.lstrip(' ')
    while ed[4] != '-' or ed[7] != ed[4] or len(ed) != 10:
        print "Please enter a date in a valid form"
        end_date = raw_input("Enter end of time period (YYYY-MM-DD): ")
        ed = end_date.lstrip(' ')    
    end_date = ed
    
    conn, c = connect_db("./hospital.db")

# SQL statement for getting the report
# grouped by drug drug category and the drug name
# the complicated part of this is the 4th column that returns the amount of the drug prescribed for a specific category
# Assumptions: Amount once again is the amount per day X the number of days
    c.execute('''SELECT d.category, m.drug_name, sum(m.amount* (cast(julianday(m.end_med) as int) - cast(julianday(m.start_med) as int))), (
            SELECT sum(m1.amount* (cast(julianday(m1.end_med) as int) - cast(julianday(m1.start_med) as int))) as total
            FROM medications m1, drugs d1
            WHERE m1.drug_name = d1.drug_name
            AND m1.mdate between date(?) and  date(?)
            and d1.category = d.category)
        FROM drugs d, medications m
        WHERE d.drug_name = m.drug_name
        AND m.mdate between date(?) and  date(?)
        GROUP BY d.category, m.drug_name
        ORDER BY d.category;''', (start_date,end_date,start_date,end_date))

    result = c.fetchall()
    
    if result == []:
        print "\nNo drugs found in that time period\n"
        return 0
    
    print "\nTotal amount of each drug prescribed in that time period, by category of drug:\n"
    # formats and prints the SQL results in  a nice way by displaying the category only once
    last_name = ""
    for row in result:
        if row[0] != last_name:
            print row[0], 'TOTAL:', row[3]
        last_name = row[0]
        print "\t",row[1],row[2]


    print
    disconnect_db(conn)

# Third option for admin, displays all medications that have been used for a diagnoses
def med_recommend():
    conn,c = connect_db()

    diagnosis = utilities.get_Admin_diagnosis()
# SQL Staement for getting the drugs that have been prescribed after a diagnoses
# COLLATE NOCASE makes the drug names case insensitive for search purposes
# gorupby and order by gives us an easy way to split each use of the drug for a diagnoses and order them by frequency
    c.execute('''SELECT m.drug_name
        FROM charts c, diagnoses d,medications m
        WHERE c.chart_id = d.chart_id
        AND m.chart_id = c.chart_id
        AND d.diagnosis = ? COLLATE NOCASE
        AND m.mdate >= d.ddate
        GROUP BY m.drug_name
        ORDER BY count(*) DESC;''', ([diagnosis])
    )

    result = c.fetchall()
    
    if result == []:
        print "\nNo medications can be suggested\n"
        return 0
    
    # This problem is a simple print as it just wants the drug names
    print "\nAll possible medications that have been prescribed over time after that diagnosis:\n"
    for row in result:
        print row[0]
    print
    disconnect_db(conn)
    
# Fourth option for admnin staff, creates a report of the amounts of each use of a drug for different diagnoses
# Prints average dosing information for length, daily dose and the total that it has been prescribed
def drug_uses():
    conn,c = connect_db()

    drug = utilities.get_medication()

# SQL Statemnt for getting the data.
# Uses the same method for determing the duration and total amounts of drugs prescribed for option 1(create)
# groups by the diagnoses and orders using an AS from the SELECT
    c.execute('''SELECT d.diagnosis, m.amount, (cast(julianday(m.end_med) as int) - cast(julianday(m.start_med) as int)), avg(m.amount* (cast(julianday(m.end_med) as int) - cast(julianday(m.start_med) as int))) as prescribeAverage
        FROM charts c, diagnoses d,medications m
        WHERE c.chart_id = d.chart_id
        AND m.chart_id = c.chart_id
        AND m.drug_name = ? COLLATE NOCASE
        AND m.mdate >= d.ddate
        GROUP BY d.diagnosis
        ORDER BY prescribeAverage DESC;

    ''', ([drug]))


    result = c.fetchall()
    if result == []:
        print "\nNo diagnoses found\n"
        return 0
    
    # fancy printing only to make the results nicely readable.
    print "\nAll the diagnoses that have been made before prescribing this drug:\n"
    for row in result:
        # print row[0] + ' Taking an average' + row[1] + 'per day for' row[2] + 'days totaling ' +row[2] + 'prescribed'
        print '%s: Taking an average %d units per day for %d days totaling %d units prescribed.' %(row[0],row[1],row[2],row[3])
    print
    disconnect_db(conn)
# drug_uses()
