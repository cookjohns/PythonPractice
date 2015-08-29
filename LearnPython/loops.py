a = 1
while a <= 100:
    print(a)
    a += 1
print('Done')

#for each
for data in [1,2,3,4,5]:
    print(data)
for s in 'string':
    print(s)
for key,data, in enumerate('string'): #key is position, data is element
    if key % 2 == 0:
        print('The letter %s is in an even location' % data)
    
tuple1 = (1,2,3,4,5)
try:
    tuple.append(6)
except AttributeError as e: 
    print('error:', e)
    output = open('errorLog.txt', 'w')
    print(e, file = output, end = '') #prints the error message to a newly created log file
else:
    for each in tuple:
        print(each)
        
list1 = [1,2,3,4,5,6,7,8,9]
for int1 in list1:
    if   int1 == 7: break
    elif int1 == 3: continue
    else:
        print(int1)
else: #does something at the end of the iteration of for loop, not necessary
    print('default')