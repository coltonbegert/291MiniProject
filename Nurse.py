from Nurse_Option_A import Nurse_Option_A
from Nurse_Option_B import Nurse_Option_B

def Nurse(sid=None):
    while 0==0:
        print"option 1, 2 and 5 work for now"
        answer = raw_input("What option would you like to choose?\n\
        (1) Create a new chart/add a patient\n\
        (2) Close a patient's chart\n\
        (3) Same as 1. for the doctors.\n\
        (4) Same as 2. for the doctors.\n\
        (5) Logout user\n\
        \nSelection: ")
        if answer == '1': 
            Nurse_Option_A()
            #Create_Chart_Add_Patient()
        
        if answer == '2': 
            Nurse_Option_B()
        '''
        if answer == '3': 
            Nurse_Option_C()
        
        if answer == '4': 
            Nurse_Option_D()
        '''
        if answer == '5':
            print '\nLogging out'
            return 0
