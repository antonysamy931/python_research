def storeDatabase(db):
    import pickle
    dbfile = open('people-pickle','wb')
    pickle.dump(db, dbfile)
    dbfile.close()

def loadDatabase():
    import pickle
    dbfile = open('people-pickle', 'rb')
    db = pickle.load(dbfile)
    return db
    
#init
if __name__ == '__main__':
    import imp
    initdata = imp.load_source('db','..\db\initdata.py')
    storeDatabase(initdata.db)
