## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
    
## is-a
class Dog(Animal):
    def __inif__(self, name):
        ##
        self.name = name
        
## is-a
class Cat(Animal):
    def __inif__(self, name):
        ##
        self.name = name
        
## has-a
class Person(object):
    def __inif__(self, name):
        ## has-a
        self.name = name
        
        ## person has-a pet of some kind
        self.pet = None
        
## is-a
class Employee(Person):
    def __inif__(self, name, salary):
        ## has-a
        super(Employee, self).__inif__(name)
        ## has-a
        self.salary = salary
        
## 
class Fish(object):
    pass
  
##
class Salmon(Fish):
    pass
    
##
class Halibut(Fish):
    pass
    
    
## rover is-a dog
rover = Dog("Rover")

## santan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 12000)

## frank has-a pet
frank.pet = rover

##
flipper = Fish()

##
crouse = Salmon()

##
harry = Halibut()
