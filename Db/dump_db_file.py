if __name__ == '__main__':
    from make_db_file import loadData, storeDatabase
    db = loadData()
    for key in db:
        print(key, '=>\n', db[key])
    db['green'] = {'name':'green', 'job':'tester', 'fathername':'test'}
    #storeDatabase(db)
