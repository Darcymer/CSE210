'''class Base:

    def __init__(self):
        self._helper()

    def _helper(self): #this is protected with 1 _, this still allows peiople to manipulate it
        print("Helper Function")
    
    def __helper(self): #this is private with two _
        print("Helper Function")

x=Base()

print ("Trying to call subfunction")

x._helper()

#print ("Trying to call private function")
#x.__helper2()

#print ("How to desatroy that above ig")
#x._Base__helper2()
'''

class Student:
    def __init__ (self,fname,lname):
        self._first = fname
        self._last = lname
    
    def show_name(self):
        return f"{self._first} {self._last}"

darcy=Student("Darcy", "Merilan")
print (darcy.show_name())


