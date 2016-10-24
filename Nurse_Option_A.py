import sqlite3
from time import gmtime, strftime

def Nurse_Option_A(hcno = None):
    #connect to the database
    conn = sqlite3.connect("./hospital.db")
    c = conn.cursor()
    
    #checks if the optional argument is blank or not
    if hcno == None:
        #get the health care number
        hcno = raw_input("Please enter patient hcno: ")
        
        # if the health care number is shorter than 5 digits or isn't 5 numbers
        if len(hcno) != 5 or hcno.isdigit() is False:
            print "Health care number is a 5 digit number"
            hcno = raw_input("Please enter patient hcno: ")
            
        # figure out if the hcno is already in the database    
        c.execute('''SELECT * FROM patients WHERE hcno=? ''', (hcno, ))
        result = c.fetchone()
        
        #if not then
        if result == None:
            print "Oops, patient not in database."
            name = raw_input("Please enter the patient's name: ")
            
            while len(name) > 15 or name.replace(' ', '').isalpha() is False or len(name.replace(' ', '')) == 0:
                
                #name is too long
                if len(name) > 15: print "Name must be 15 characters or shorter."
                
                if name.replace(' ', '').isalpha() is False and len(name.replace(' ', '')) != 0:    #name contains numbers and is not blank
                    print "Name must not contain numbers"          #when I left the blank check out, it popped up when this was empty
                    
                #name contains entirely spaces   
                if len(name.replace(' ', '')) == 0:  print "Name can't be blank"
                
                name = raw_input("Please enter the patient's name: ")
            
            name = name.title() #capitalize first letter of each word and lowercase the rest
            
            #get age group
            print "Now we need the age group. To make it homogeneous with the others we have"
            
            #find all the current age groups in the database
            c.execute('''
            SELECT DISTINCT age_group FROM patients ORDER BY age_group ;
            ''')
            resultat = c.fetchall()
            result = [str(x).strip("(u',)") for x in resultat] #get rid of the annoying formatting they seem to come with
            result.append("Custom") #add the option to add an age group to the database
            
            # generate the numbers in the (x) part of the output
            for i in range(1, len(result)+1):
                x = result[i-1]
                print "(" + str(i) + ")  " + str(x)
                
            
            answer = raw_input("Enter your selection: ") #still to add: make sure you got a number in the list, and that it's a number
            
            #if they didn't choose custom
            age_group = result[int(answer)-1]
            
            #if they choose custom
            if answer == str(len(result)):
                exit = False
                while exit == False:
                    #gets the low and high range of the age group and then concatenates them
                    age_group_low = raw_input("Enter the lowest age in the group: ")
                    age_group_hi = raw_input("Enter the highest age in the group: ")
                    age_group = str(age_group_low).zfill(2) + '-' + str(age_group_hi).zfill(2) #zfill(2) enter 3 and it becomes 03, 8 becomes 08 and 10 remains 10
                    test = raw_input("Add age group to db (y/n/exit)? : ")
                    if test.lower().replace(' ', '') == 'exit':
                        exit = True
                    elif test.lower().replace(' ','') == 'y':
                        exit = True
            address = raw_input("Please enter their address: ")
            while len(address)>30:
                print "address must be shorter than 31 characters"
                address = raw_input("Please enter their address: ")
            
            phone = raw_input("Please enter phone number, format: 00000000000: ")
            while phone.isdigit() is False or len(phone) > 10:
                if phone.isdigit() is False:
                    print "Please enter only digits"
                if len(phone) > 10:
                    print "Please limit to 10 digits"
                
                phone = raw_input("Please enter phone number, format: 00000000000: ")
            
            emg_phone = raw_input("Please enter emergency contact number.\n If it's the same as your phone number, just enter 's'")
            if emg_phone.lower() == 's':
                emg_phone = phone
            while phone.isdigit() is False:
                print "Please enter only digits or 's'"
                emg_phone = raw_input("Please enter emergency contact number.\n If it's the same as your phone number, just enter 's'")
                if emg_phone.lower() == 's':
                    emg_phone = phone 
            
            insertion = [(hcno, name, age_group, address, phone, emg_phone)]
            c.executemany('INSERT INTO patients VALUES (?,?,?,?,?,?)', insertion)
            conn.commit()
            

    #selects the first unused chart number from 00001 to 99999
    c.execute('SELECT chart_id FROM charts WHERE hcno=:hcno AND edate=:edate ORDER BY adate DESC', {'hcno':hcno, 'edate':'Null'})
    chart_id = str(c.fetchone()).strip("(u',)")
    
    if chart_id != str(None):
        print "Found chart with chart id", chart_id
        question = raw_input("Would you like to close this chart and open a new one(Y/N)?: ")
        if question.upper() == 'Y':
            edate = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            c.execute('UPDATE charts SET edate=:edate WHERE chart_id=:chart_id', {'edate':edate, 'chart_id':chart_id} )
            conn.commit()
        else:
            print "The chart stays open"
            return 0
            
        
        
    for i in range(1, 100000):
        chart_id = str(i).zfill(5) #what zfill does: 1 turns into 00001, 100 turns into 00100, 10000 and higher remain the same
        chart_id_format = (chart_id, )
        c.execute('''SELECT * FROM charts WHERE chart_id=? ''', chart_id_format)
        result = c.fetchone()
        if result == None:
            break
    
    adate = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    insertion = [(chart_id, hcno, adate, 'Null')]
    try:
        c.executemany('INSERT INTO charts VALUES (?,?,?,?)', insertion)
        conn.commit()
        print "\nCreated new chart for patient with following information:"
        print "----------------------------------------------------------"
        print "Chart ID:           ", chart_id
        print "Health Care Number: ", hcno
        print "Date Opened:        ", strftime("%A, %d %B %Y %H:%M:%S", gmtime())
        print "----------------------------------------------------------"
    except:
        print "Something went wrong while storing or printing the chart information"