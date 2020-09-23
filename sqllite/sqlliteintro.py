import _sqlite3

def main():
    try:
        mydb = _sqlite3.connect(database = 'namelist')
        print('Created a database')

    except:
        print('Could not create a database')

    mydb.close()

if __name__ == '__main__':
    main()