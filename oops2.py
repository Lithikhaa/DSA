# Introduction to class and objects

class Vehicle:
    def __init__(self,companyname,wheelertype,brandname):
        self.companyname = companyname
        self.wheelertype = wheelertype
        self.brandname = brandname
        
    def Println(self):
        print(self.wheelertype)
        
    def checkingtype(self):
        if self.wheelertype == 'fourwheeler':
            print('It is a car')
        else:
            print('It is a bike')
        
obj1 = Vehicle('ferrari','Twowheeler','vollswegan')
obj1.Println()
obj1.checkingtype()

# Inheritence


# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Single Inheritence , Single inheritance enables a derived class to inherit properties from a single parent class

class Vehicle:
    def __init__(self,companyname,wheelertype,brandname):
        self.companyname = companyname
        self.wheelertype = wheelertype
        self.brandname = brandname
        
    def Println(self):
        print(self.wheelertype)
        
    def checkingtype(self):
        if self.wheelertype == 'fourwheeler':
            print('It is a car')
        else:
            print('It is a bike')
        
        
class Environment(Vehicle):
    
    def typeofvehicle(self):
        if self.wheelertype == 'twowheeler':
            print('This is bike')
        elif self.wheelertype == 'fourwheeler':
            print('This is car')
        else:
            print('This is Aeroplane')
    
  
obj1 = Environment('ferrari','twowheeler','vollswegan')
obj1.Println()
obj1.typeofvehicle()

# Multi-Level Inheritence , features of the base class and the derived class are further inherited into the new derived class.

class Vehicle:
    def __init__(self,companyname,wheelertype,brandname):
        self.companyname = companyname
        self.wheelertype = wheelertype
        self.brandname = brandname
        
    def Println(self):
        print(self.wheelertype)
        
    def checkingtype(self):
        if self.wheelertype == 'fourwheeler':
            print('It is a car')
        else:
            print('It is a bike')
        
        
class Environment(Vehicle):
    
    def typeofvehicle(self):
        if self.wheelertype == 'twowheeler':
            print('This is bike')
        elif self.wheelertype == 'fourwheeler':
            print('This is car')
        else:
            return 'Aeroplane'
            
class Bigvehicle(Environment):
    
    def morethan_fourwheeler(self):
        if self.typeofvehicle() == 'Aeroplane':
            print('It contains more than 10 wheels')
            
        else:
            print('It contain 6 wheels')
    
obj1 = Bigvehicle('ferrari','Aeroplane','vollswegan')
obj1.Println()
obj1.typeofvehicle()
obj1.morethan_fourwheeler()



#Multiple Inheritance , When a class can be derived from more than one base class this type of inheritance is called multiple inheritances

class Maths:
    
    def Addition(self,a,b):
        return a+b
    
    def subtraction(self,a,b):
        return a-b
    
class Complex_maths:
    
    def Multiplication(self,a,b):
        return a * b
    
class Advanced_maths(Maths,Complex_maths):
    def divide(self,a,b):
        return a // b
    
obj1 = Advanced_maths()
obj1.Addition(11,5)
print(obj1.divide(5,5))

        

# Hierarchical inheritance , When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.

class Parent:
	def func1(self):
		print("This function is in parent class.")


class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")


class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
