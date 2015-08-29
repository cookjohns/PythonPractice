list = [8,7,12,4,9,6,5]
#perform bubble sort
len = len(list)
i = 0
while i < len:
    j = 0
    while j < len-1:
        if list[j] > list[j+1]:
            c = list[j]
            list[j] = list[j+1]
            list[j+1] = c
        j = j+1
    i = i+1
print(list)
    