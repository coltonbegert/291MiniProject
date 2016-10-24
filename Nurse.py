from Nurse_Option_A import Nurse_Option_A

def Nurse(sid):
    while 0==0:
        print"only option 1 and 5 work for now"
        answer = raw_input("What option would you like to choose?\n\
        (1) Create a new chart/add a patient\n\
        (2) Close a patient's chart\n\
        (3) Same as 1. for the doctors.\n\
        (4) Same as 2. for the doctors.\n\
        (5) Logout\n\
        \nSelection: ")
        if answer == '1':
            Nurse_Option_A()
        if answer == '5':
            print '\nLogging out'
            return 0