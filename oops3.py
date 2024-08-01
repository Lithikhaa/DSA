#Encapsulation --> Encapsulation is a way to protect and organize data
# A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc. 
# The goal of information hiding is that an object’s state is always controlling access to attributes that are hidden from the outside world.

# Eg : Transaction --> if a person send a money, there is a backend code which will be encapsulated, which can prevent the users detail from others.
'''
Different Sections in a Company: A company has various sections like accounts, finance, and sales.

Section Responsibilities: Each section handles its own tasks and keeps its own records.
Finance Section: Manages financial transactions and records.
Sales Section: Manages sales activities and records.

Need for Data Sharing: Sometimes, one section (e.g., finance) needs information from another section (e.g., sales).
Access Restrictions:
An official from the finance section cannot directly access sales data.
They must request the data from an authorized person in the sales section.

Encapsulation:
Each section's data and the people who can access it are grouped together.
Data is hidden from other sections, ensuring controlled access.

Encapsulation in summary: It's like each section having its own locked room, and only certain people have the keys. 
To get information, you need to ask someone with the key. This keeps the data secure and organized. '''

#without private
class Payment:
    
    def __init__(self,username, payamount,balance,paymentnum):
        self.username= username
        self.payamount = payamount
        self.balance = balance
        self.paymentnum = paymentnum
       
#  Private Access: Only accessible within the same class where it is declared.

    def transaction(self):
        amount = 500
        if amount == self.payamount:
            print('The amount have been successfully paid')
        else:
            print('The Transaction is failed',self.paymentnum)
        
# Protected Access: Accessible within the same class and by subclasses (derived classes).

class Saving_account(Payment):
    
    def sav_acc(self):
        balance = self.balance - self.payamount
        print(balance)
        
    
obj1 = Saving_account('Lithi',50,1000,2426)

obj1.transaction()
obj1.sav_acc()
        
    
#with private
class Payment:
    
    def __init__(self,username, payamount,balance,paymentnum):
        self.username= username
        self.payamount = payamount
        self.balance = balance
        self.__paymentnum = paymentnum    #private key  -- __
       
#  Private Access: Only accessible within the same class where it is declared.

    def transaction(self):
        amount = 500
        if amount == self.payamount:
            print('The amount have been successfully paid')
        else:
            print('The Transaction is failed',self.paymentnum)
        
# Protected Access: Accessible within the same class and by subclasses (derived classes).

class Saving_account(Payment):
    
    def sav_acc(self):
        balance = self.balance - self.payamount
        print(balance)
        
    
obj1 = Saving_account('Lithi',50,1000,2426)

obj1.transaction()
obj1.sav_acc()
        
# with protected
class Payment:
    
    def __init__(self,username, payamount,balance,paymentnum):
        self.username= username
        self._payamount = payamount
        self.balance = balance
        self.paymentnum = paymentnum
       
#  Private Access: Only accessible within the same class where it is declared.

    def transaction(self):
        amount = 500
        if amount == self._payamount:
            print('The amount have been successfully paid')
        else:
            print('The Transaction is failed',self.paymentnum)
        
# Protected Access: Accessible within the same class and by subclasses (derived classes).

class Saving_account(Payment):   #here inherit another class so it is protected
    
    def sav_acc(self):
        balance = self.balance - self._payamount        #_payamount ---> protected _
        print(balance)
        
    
obj1 = Saving_account('Lithi',50,1000,2426)

obj1.transaction()
obj1.sav_acc()
        
# without protected
class Payment:
    
    def __init__(self,username, payamount,balance,paymentnum):
        self.username= username
        self._payamount = payamount
        self.balance = balance
        self.paymentnum = paymentnum
       
#  Private Access: Only accessible within the same class where it is declared.

    def transaction(self):
        amount = 500
        if amount == self._payamount:
            print('The amount have been successfully paid')
        else:
            print('The Transaction is failed',self.paymentnum)
        
# Protected Access: Accessible within the same class and by subclasses (derived classes).

class Saving_account:   #here not inherit the another class so it is protected , so u will getin a error
    
    def sav_acc(self):
        balance = self.balance - self._payamount        #_payamount ---> protected
        print(balance)
        
    
obj1 = Saving_account('Lithi',50,1000,2426)

obj1.transaction()
obj1.sav_acc()
        
    
    
    