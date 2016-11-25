#File read function

filename = "D:\Antony\Python\while_loop.py"
try:
    fobj = open(filename,'r')
    data = fobj.readlines()
    fobj.close()
    for eachline in data:
        print(eachline)
except IOError as e:
    print("error in %s ",(e))
