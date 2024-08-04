#Method Overloading
# Method overloading is the ability to define multiple methods with the same name but with different parameters
# However, Python does not support method overloading directly like some other languages (e.g., Java). 
# Instead, you can achieve similar behavior using default arguments or variable-length arguments.

def calculate(a,b,c=0):
    return a+b+c

print(calculate(5,2))
print(calculate(5,5,5))

#Method Overriding
# Method overriding is when a subclass provides a specific implementation for a method that is already defined in 
# its superclass. This allows the subclass to modify or extend the behavior of the superclass method

class calculate:                                          #superclass
    def ad(self,a,b):
        print(a+b)
        
class advanced_calculation(calculate):                     #subclass
    def sub1(self,a,b):
        print(a-b)
        
    def ad(self,a,b):
        print(a-b)
        
    # def add(self,a,b):
    #     print(a+b)
        
obj1 = advanced_calculation()
obj1.ad(2,1)

