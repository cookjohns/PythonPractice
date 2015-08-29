def myFunction():
    "This is a tagline" #does not print
    return 'Hello'

#print(myFunction())

list = [1,2,3,4]
def listAdd(listIn):
    "Params passed by reference"
    listIn.append([5,6,7,8])
    return

def listAddDef(listIn, addIn):
    "Params passed by reference"
    listIn.append(addIn)
    return

#print(list)
listAdd(list)
#print(list)

x = [9,10]
listAddDef(list, x)
#print(list)

def func():
    x = 1 #returns None
def func1():
    return #returns None
def func2():
    return 'Hello' #returns Hello
    
print(func())
var = func()
if var == None: #None is a keyword
    print('true')