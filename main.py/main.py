import csv 
data_base =[]
#importing validation and options
from validation import *
from options import *

#main system menu
def menu () :
    print("1. REGISTER NEW STUDENTS")
    print("2. VIEW THE  STUDENT LIST")
    print("3. SEARCH FOR THE STUDENT")
    print("4. UPDATE STUDENTS")
    print("5. DELETE STUDENTS")
  
def main ( ) :
    print ("BIENVENIDOS ")
    running = True
    while running :
        
        option = menu ()
        option = pedirNumero ("ENTER THE OPTION NUMBER: ", "int")
        if option == 1: 
            addStudents ()
        elif option == 2:
            SeeStudents ()    
        elif option == 3:
            Search ()
        elif option == 4: 
            updateInformation()
        elif option == 5: 
            delete ()
        elif option == 6: 
            print ("exit")
        
            print("Program finished.")
            return menu
            
    
        else:
        
           print ("Invalid option, try again.")

main ()           
