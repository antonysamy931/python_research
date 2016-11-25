#File read function
filename = "D:\Antony\Python\while_loop.py"
fobj = open(filename,'r')
data = fobj.readlines()
fobj.close()
for eachline in data:
    print(eachline)
