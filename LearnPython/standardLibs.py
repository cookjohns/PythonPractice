import datetime
import sys
import os

now = datetime.datetime.now()

#print(now)

# time a Function

start = datetime.datetime.now()

i = 0
while i < 100000:
    i = i + 1
    
end = datetime.datetime.now()

print(end - start) #prints time that the loop took to run


print(sys.path) #prints current dir
print(os.name)  #prints 'posix' (name for Unix systems)
