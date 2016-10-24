import sqlite3
from Build_Database import Build_Database
from time import gmtime, strftime

Build_Database()
conn = sqlite3.connect("./hospital.db")
c = conn.cursor()


c.execute('SELECT chart_id FROM charts WHERE edate is Null') #selects all open charts (ie. all charts where the release date (edate) are Null)
print(c.fetchone()) #prints the id of the first open chart


#creating a new open chart
chart_id = '99999'
hcno = '15384'
adate = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #current time
insertion = [(chart_id, hcno, adate, None)]

c.executemany('INSERT INTO charts VALUES (?,?,?,?)', insertion)
conn.commit()


