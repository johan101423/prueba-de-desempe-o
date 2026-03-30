data_base =[]
from validation import *
# START OF OPTIONS FUNCTIONS
def addStudents () :
    id = input ("ENTER ID OF STUDENTS : ")
    name= input ("ENTER NAME OF STUDENTS :")
    age = input ("ENTER AGE OF STUDENTS :")
    program = input ("NAME OF PROGRAM : ")
    state = input ("ACTIVE OR INACTIVE: ")
    list ={id ,  
           name ,
          age ,
          program ,
           state          
         } 
    data_base.append  (list) 
list
def SeeStudents () : 
          
          for  id,name ,age ,program , state  in data_base:
           print (f"ID :{id}")
           print (f" NAME : {name}")
           print (f"AGE :{age}")
           print (f"PROGRAM : {program}")
           print (F"STATE  : {state}") 
           
print ("STUDENTS NOT FOUND")   

def Search () :  
     Search =input ("NAME OF STUDENTS TO SEARCH :")      
     for  id,name ,age ,program , state   in data_base :
          print (f"ID{id}")
          print (f" NAME {name}")
          print (f"AGE{age}")
          print (f"PROGRAM {program}")
          print (F"STATE {state}") 
          return
     print ("STUDENTS NOT FOUND")
def updateInformation () :
        name =input ("NAME OF THE STUDENTS UPDATE : ")
        for name  in data_base :
              data_base.remove (name)
              print ("ENTER NEW DATA")
              addStudents ()
              return
        print ("STUDENTS NOT FOUND.")

def delete () :
     name =input ("NAME OF THE STUDENTS UPDATE : ")
     for name in data_base :
              data_base.remove (name)
              print ("students removed")
              return
     print ("STUDENTS NOT FOUND")

