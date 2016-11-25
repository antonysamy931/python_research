#membership operator in python

a = 10
b = 20
listvalue = [1,2,3,4,5]

if(a in listvalue):
    print('a value in list')
else:
    print('a value not in list')
    
if(b not in listvalue):
    print('b value not in list')
else:
    print('b value in list')
    
a = 2

if(a in listvalue):
    print('a value in list')
else:
    print('a not in list')   