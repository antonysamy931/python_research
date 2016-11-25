if __name__ == '__main__':
    from make_db_file import loadDatabase
    records = loadDatabase()
    print(len(records))
