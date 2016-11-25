#initial file name and tabs
fileName = 'people-file'
ENDDB = 'enddb'
ENDREC = 'endrec'
RECSEP = '|'

#Stroe data to db file
def storeDatabase(db, dbfilename = fileName):
    "formatted dumb of database in flat file"
    dbfile = open(dbfilename,'w')
    for key in db:
        print(key, file=dbfile)
        for (name,value) in db[key].items():
            print(name+RECSEP+repr(value),file=dbfile)
        print(ENDREC,file=dbfile)
    print(ENDDB,file=dbfile)
    dbfile.close()

#load data from db file
def loadData(dbfilename = fileName):
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = value
            field = input()
        db[key] = rec
        key = input()
    dbfile.close()
    return db

#As script run serve first method
if __name__ == '__main__':
    from initdata import db
    storeDatabase(db)
