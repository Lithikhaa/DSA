#Abstraction
'''Data abstraction is one of the most essential concepts of Python OOPs which is used to hide irrelevant details
from the user and show the details that are relevant to the users'''


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__engine_status = 'off'  # Private attribute

    def start_engine(self):
        self.__engine_status = 'on'                       #this is hidden info which user need not to known
        print(f'{self.make} {self.model} engine started.')          #this is not hiddent bcoz user need to know abt it.

    def stop_engine(self):
        self.__engine_status = 'off'
        print(f'{self.make} {self.model} engine stopped.')

    def drive(self):
        if self.__engine_status == 'on':                                  
            print(f'{self.make} {self.model} is driving.')
        else:
            print(f'{self.make} {self.model} engine is off. Please start the engine first.')

# Usage
my_car = Car('Toyota', 'Corolla')
my_car.start_engine()
my_car.drive()
my_car.stop_engine()
