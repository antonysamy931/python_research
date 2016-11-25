#identity operator in python

a = 20
b = 20

if(a is b):
    print('a is same identity as b')
else:
    print('a is not same identity as b')

if(id(a) == id(b)):
    print('a is same identity as b')
else:
    print('a is not same identity as b')
    
b = 1

if(a is not b):
    print('a is not same identity as b')
else:
    print('a is same identity as b')                      