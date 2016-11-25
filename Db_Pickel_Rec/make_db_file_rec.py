def storeDatabase(db):
    import pickle
    for key in db:
        recFile = open(key+ '.pkl','wb')
        pickle.dump(db[key],recFile)
        recFile.close()

def loadDatabase():
    import pickle, glob
    db={}
    for filename in glob.glob('*.pkl'):
        recfile = open(filename, 'rb')
        record = pickle.load(recfile)
        key = filename.split('.')[0]        
        db[key] = record
    return db

if __name__ == '__main__':
    import imp
    modules = imp.load_source('db','..\db\initdata.py')
    #storeDatabase(modules.db)
    loadDatabase()
    
