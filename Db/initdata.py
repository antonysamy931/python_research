#record
antony = {'name':'Antony', 'job':'developer', 'fathername':'joseph'}
jai = {'name':'jai', 'job':'programmer', 'fathername':'jai'}

#database
db = {}
db['antony'] = antony
db['jai'] = jai

#when run as a script starting point
if __name__ == '__main__':
    for key in db:
        print(key, '=>\n ', db[key])
