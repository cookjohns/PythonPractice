def checkType(input):
    if isinstance(input, bool):
        return 'Boolean'
    elif isinstance(input, int):
        return 'Digit only'
    elif isinstance(input, str):
        return 'Alphanumeric'
    
a = True
b = 12345678
c = '1234asdf'

print(checkType(a))
print(checkType(b))
print(checkType(c))