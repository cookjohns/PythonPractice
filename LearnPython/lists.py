list = [1,2,3,4,5,6,7,8,9,10,11] #can modify, not immutable
print(list)
print(list[2])
print(list[-3]) #goes backwards from the start
print(len(list)) #prints length of list
len = len(list)
var = len - 4
print(var) #prints 4th item from the end of list, 7
print(list[2:5]) #prints values 2 - 5, stops at one less
print(list[0:10:2]) #stepper, by 2 (from 1 to 10), prints odds
print(list[::2]) #from beginning, all of list, step by 2 (print all odds)

list.append(12)
list2 = [13,14]
list.extend(list2)
list.insert(3, 12)
list[0] = list[2] *2
del list[2:3]
list.remove(6) #removes the first 6, so the second one is still there

list.reverse() #prepend func doesn't exist, reverse, add, reverse
list.append(0)
list.reverse()
print(list)

rand = [1,3,4,2,5]
rand.sort()
print(rand)
sortedRand = sorted(rand)
print(sortedRand)