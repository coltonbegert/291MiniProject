import sqlite3

def Admin():
    print "1) Create Report\n2) prescribed\n3) medication recommendation\n4) Drug uses\n"
    needInput = True
    while needInput:
        option = raw_input("Choose and option: ")
        if option <='4' or option >'0':
            needInput = False
        elif option == "exit":
            needInput = False
            break
        else:
            print "incorrect option. Try again or type 'exit' to exit"
            continue

        print type(option)
        if option == '1':
            createReport()
        elif option == '2':
            prescribed()
        elif option == '3':
            medRecommend()
        elif option == '4':
            drugUses()

def connect_db(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    return conn, c

def disconnect_db(conn):
    conn.commit()
    conn.close()
    return

def createReport():
    print "Define time period"
    start_date = raw_input("Enter start of time period (YYYY-MM-DD): ")
    end_date = raw_input("Enter end of time period (YYYY-MM-DD): ")
    # start_date = '2000-01-01'
    # end_date = 'now'
    conn, c = connect_db("./hospital.db")

    c.execute('''SELECT s.name, m.drug_name, sum(m.amount* (cast(julianday(m.end_med) as int) - cast(julianday(m.start_med) as int)))
        FROM staff s, medications m
        WHERE m.staff_id = s.staff_id
        AND m.mdate between date(?) and  date(?)
        GROUP BY s.name, m.drug_name
        HAVING s.role = 'D'
        ORDER BY s.name;''', (start_date,end_date))

    result = c.fetchall()
    last_name = ""
    for row in result:
        if row[0] != last_name:
            print row[0]
        last_name = row[0]
        print "\t",row[1],row[2]




    disconnect_db(conn)

def prescribed():
    conn,c = connect_db("./hospital.db")



    disconnect_db(conn)

Admin()
