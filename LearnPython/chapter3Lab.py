a = True
b = True
c = True
q = True

if a & b:
    q = 1
print(q)

if a or b: q = 1
print(q)

# a and not b or c = q
if a & (not b & (not c)):
    q = True
else: q = False

def test(aIn, bIn, cIn):
    if a & (not b & (not c)):
        return True
    else: return False
    
q = test(a, b, c)
print(q)