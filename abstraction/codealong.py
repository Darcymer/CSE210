'''
#1 1/19/2022 Abstraction

# Class are making an abstraction (diffrent way of thinking of the same thing) that makes things....
# Class can be Animals, and we can link dogs and cats to that class
class Person:
    pass


#python notations are...... interesting, as you can add variables to anything ... becareful
Darcy = Person()
print(Darcy)

Darcy.full_name ="Darcy Merilan"
print(Darcy.full_name)
#--------------------------
'''

'''class Person:
    def _init_(self): #_init_ is a constructor, self is self, NEVER change it(you can but there is no point), 
        pass          #but you can have more

Darcy = Person()
print(Darcy)

Dupond = Person()
print(Dupond)
#--------------------------
'''
''' This has an error
class Person:
    def _init_(self, full_name = ""): #if we want to make full_name optional you can do def _init_(self, full_name ="")~ the "" can be filled but the program will think if the name dosent have anything, it will fill it in with whatever is in the  ""
        self.full_name = full_name       

Darcy = Person("Darcy Merilan")
print(Darcy)
print(Darcy.full_name)

Dupond = Person("Darcy Merilan")

print(Dupond.full_name)
#------------------'''
class Person:
    def __init__(self,Full_name):
        self.full_name

class Restaurant:

    def __init__(self,name,cuisine,price,rating):
        self.name = name
        self.cuisine = cuisine
        self.price = price
        self.rating = rating
    
    def __str__(self):
        return self.name

