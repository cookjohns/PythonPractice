a,b = 0,1
if a == b or a <= b: #not =<
    print(True)
if a != b:
    print(False)
    
if a == b:
    print(True)
else:
    print(False)
    
switch = dict(
              one = 1,
              two = 2)
var = 'one' 
print(switch[var]) #prints 1
var = 'three'
print(switch.get(var, 'default')) #prints 'default'

var = '7' if a == b else '12' #in java: a == b ? var = '7' : var = '12'
print(var)