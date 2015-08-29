code = '82914656273523:a4edFea2786DGex'
#format is id:key
#id is digits of len 14
#key may contain chars, len 10-20
temp = code.split(':')
id = temp[0]
key = temp[1]
allNums = True

#run check here
for i in id:
    if not(i.isdigit()):
       allNums = False 
if len(id) != 14:
    print('Invalid id')
elif allNums == False:
    print('Invalid id')
elif len(key) < 10 or len(key) > 20:
    print('Invalid key')
else:
    print('All is good')