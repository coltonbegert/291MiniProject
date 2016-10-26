import sqlite3



def Admin_Option_C():

	conn = sqlite3.connect("./hospital.db")
	c = conn.cursor()

	Diagnosis = raw_input("Enter Diagnosis")

	# execute SQL STATEMENT get time

	c.execute(''' SELECT ddate from diagnoses where diagnosis = Diagnosis; ''')

	c.fetchall()

	c.execute('''SELECT m.drug_name from medications m, diagnosis d where  m.hcno = d.hcno and datetime(ddate) > date(timespecified)''')
	c.fetchall()

	# print all possible medications that have been preserived over time after specifed diagnosis 
	for x in list:
		print(x)

	
