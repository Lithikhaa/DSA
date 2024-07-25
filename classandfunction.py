
#Class
class Detail:
    def __init__(self,name,section,rollno):
        self.name = name
        self.section = section
        self.rollno = rollno
        
    def println(self):
        print(self.name)
        
obj1 = Detail('Lithi','B',55)
obj2 = Detail('lithipapa','C',50)
obj2.println()

# Function
def getdetail(name,rollno,sec,social,maths):
    return name,rollno,sec,social,maths
def avgmarks(social,maths):
    avg = social
print(getdetail('lithi',55,'B',99,78))


#without __init__
class Student:
    def getinput(self):
        self.name  = input()
        self.rollno = int(input())
        self.sec = input()
        
    def printdetails(self):
        print(self.rollno)      
obj3 = Student()
obj3.getinput()
obj3.printdetails()


#with __init__
class Student:
    def __init__(self,name):
        self.name  = name
        # self.rollno = int(input())
        # self.sec = input()
        
    def printdetails(self):
        print(self.name)    
        
name = 'lithi'  
obj3 = Student(name)
obj3.printdetails()



# Functions
def student():
    name = input()
    sec = input()
    rollno = int(input())
    maths = int(input())
    cs = int(input())
    
def avg_marks(maths,cs):
    avg = (maths+cs)/2
    return avg

student()
print(avg_marks(50,50))

#class

#without constructor
class Student:
    def getdetails(self):
        self.name = 'lithi'
        self.sec = 'b'
        self.rollno = 55
        self.maths = 50
        self.cs = 50
        
    def avg_marks(self,maths,cs):
        avg = (self.maths + self.cs)/2
        return avg
    def roll_no(self):
        print(self.rollno)
obj1 = Student()
obj1.getdetails()
obj1.rollno = 75
print(obj1.avg_marks(100,100))
obj1.roll_no()

#using constructor
class Student:
    def __init__(self,name,sec,rollno,maths,cs):
        self.name = name
        self.sec = sec
        self.rollno = rollno
        self.maths = maths
        self.cs = cs
    def avg_marks(self):
        avg = (self.maths+self.cs)//2
        print(avg)
        
obj1 = Student('lithi','B',55,100,100)
obj1.avg_marks()
        


# Problem 1
class Student:
    def __init__(self,name,sec,rollno,maths,phy,cs):
        self.name = name
        self.sec = sec
        self.rollno = rollno
        self.maths = maths
        self.phy = phy
        self.cs = cs
        
    def avg_marks(self):
        self.avg = (self.maths+self.phy+self.cs)//3
        
    def calculate(self):
        if self.avg < 45:
            print('The student is Fail')
        else:
            print('The student is Pass')
            
obj1 = Student('lithi','B',55,79,89,90)
obj2 = Student('girlie','C',58,19,19,90)
obj1.avg_marks()
obj1.calculate()  
obj2.avg_marks()
obj2.calculate()      

class Student:
    def __init__(self,name,sec,rollno,maths,phy,cs):
        self.name = name
        self.sec = sec
        self.rollno = rollno
        self.maths = maths
        self.phy = phy
        self.cs = cs
        
    def avg_marks(self):
        self.avg = (self.maths+self.phy+self.cs)//3
        if self.avg < 45:
            print('The student is Fail')
        else:
            print('The student is Pass')
            
obj1 = Student('lithi','B',55,79,89,90)
obj2 = Student('girlie','C',58,19,19,90)
obj1.avg_marks()
obj2.avg_marks()
   