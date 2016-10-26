import sqlite3

def Admin():
    print "1) Create Report\n2)prescribed\n3)medication recommendation\n4)Drug uses\n"
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
    start_date = raw_input("Enter start of time period (YYYY-MM-DD HH:MM:SS): ")
    end_date = raw_input("Enter end of time period (YYYY-MM-DD HH:MM:SS): ")
    conn, c = connect_db("./hospital.db")

    c.execute('''SELECT s.name, m.drug_name, sum(m.amount* (julianday(m.start_med) - julianday(m.end_med))
        FROM staff s, medications m
        WHERE m.staff_id = s.staff_id
        AND m.mdate between date(day0=:day0) and  date(day1=:day1)
        GROUP BY s.name, m.drug_name
        HAVING s.role = 'D'
        ORDER BY s.name;''', {'day0':start_date, 'day1':end_date})
    for row in c.fetchall():
        print row



    disconnect_db(conn)

Admin()
