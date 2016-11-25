def storeDatabase(dbobj):
    import shelve
    db = shelve.open('people-shelve')
    for key in dbobj:
        db[key] = dbobj[key]
    db.close()

def loadDatabase():    
    import shelve
    db = shelve.open('people-shelve')
    dbobj = {}
    for key in db:        
        dbobj[key] = db[key]
    db.close()
    return dbobj

def addRecords(records):
    import shelve
    db = shelve.open('people-shelve')
    for key in records:        
        db[key] = records[key]
    db.close()

if __name__ == '__main__':
    import imp
    modules = imp.load_source('db','..\db\initdata.py')
    storeDatabase(modules.db)
