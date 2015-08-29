class Person:
    def __init__(self, gender, name): #constructor
        self.gender = gender
        self.name = name    
    def display(self):
        print('You are a', self.gender, 'named', self.name, '.')
    def show(self):
        self.display()
        
        
john = Person('male', 'John')
#john.display()
#john.show()

class Example:
    def __init__(self, **kwargs): # **stores as dict, *stores as tuple
        self.variables = kwargs   # set up all class variables here
    def setVars(self, k, v):
        self.variables[k] = v
    def getVars(self, k):
        return self.variables.get(k, None) #if val not found, return None (default val)
        
x = Example(Age = 17)
x.setVars('name', 'john')
print(x.getVars('name'))
print(x.getVars('Age'))

class Animal:
    def talk(self):
        print('Hello')
    def eat(self):
        print('Ate')
class Cat(Animal):
    def talk(self):
        print('Meow')
        super(Cat, self).talk()
    def move(self):
        print('moved')
class Dog(Animal):
    pass
    
smokey = Cat()
smokey.talk()
smokey.eat()
dog = Dog()
dog.talk()