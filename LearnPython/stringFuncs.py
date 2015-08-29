#string = ['s','t','r','i','n','g'] #these are the same
#string = 'string'
#print(string[:4:2])
from _ast import List

#for letter in string:
    #print(letter)
    
string = 'this is a string with the letter s in it.'
sCount = string.count('s')
#print(sCount)
#print(string.title()) #caps all first letters of words
#print(string.capitalize()) #caps first letter of string

string = '-'
sequence = ['a','b','c','d','e','f']
print(string.join(sequence)) #put string between each thing in the sequence

s = 'a-b-c-d-e-f'
print(s.split('-')) #split string by '-' into a List
list = s.split('-')
print(s[2]) #prints b