# Polymorphism

# What is Polymorphism: The word polymorphism means having many forms. 
# In programming, polymorphism means the same function name (but different signatures) being used for different types. 

'''Eg :

here polymorphism is example for len , bcoz len supports different datatypes(strings,list)
len() being used for a string
print(len("geeks"))

len() being used for a list
print(len([10, 20, 30]))'''


def add(x, y, z=0 ): 
    return x + y+z

print(add(2, 3))
print(add(2, 3, 4))


class Bird:
  def intro(self):
    print("There are many types of birds.")
    
  def flight(self):
    print("Most of the birds can fly but some cannot.")
  
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
    
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
    
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()






'''Create a base class Animal with a method make_sound. Then, create two subclasses Cat and Cow, each overriding the make_sound
method to provide specific implementations. Finally, write a function that takes a list of animals 
and calls the make_sound method for each animal, demonstrating polymorphism.

Requirements:
Define a base class Animal with a method make_sound that prints a generic message like "Some generic animal sound".
Define a subclass Cat that overrides the make_sound method to print "Meow".
Define a subclass Cow that overrides the make_sound method to print "Moo".
Create a function play_sounds that takes a list of Animal objects and calls the make_sound method for each object.
Example Usage:'''
  
class Animal:
  def make_sound(self):
    print('Some generic animal sound')
    
class Cat(Animal):
    
  def make_sound(self):
    print('meowwwww')
    
class Cow(Animal):
  def make_sound(self):
    print('moooo')
    
def play_sounds(obj1):
  for animals in obj1:
     animals.make_sound()
    
    
obj1 = [Cat(), Cow(), Animal()]

play_sounds(obj1)