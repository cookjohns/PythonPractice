file = open('data.txt') 
    
input  = open('data.txt', 'r')
output = open('new.txt', 'w')  #creates a file that does not yet exist

#for line in input:
    #print(line, end = '')

#for line in input:
    #print(line, file = output, end = '') #prints to output file
    
bufferSize = 100000
bufferLimit = 1000000
infile = open('bigfile.txt', 'r')
outfile = open('newbigfile.txt', 'w')
buffer = infile.read(bufferSize)

#while bufferLimit > 0:
    #outfile.write(buffer)
    #print('.', end = '')
    #buffer = infile.read(bufferSize)
    
bufferSize = 100000
input2 = open('keyboard_bokeh.jpg', 'rb')
output2 = open('image2.jpg', 'wb')
buffer = input2.read(bufferSize)

while len(buffer):
        output2.write(buffer)
        print('.', end = '')
        buffer = input2.read(bufferSize)