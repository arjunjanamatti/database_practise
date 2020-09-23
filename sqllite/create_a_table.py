import _sqlite3

def main():
    try:
        mydb = _sqlite3.connect(database = 'namelist')

        cur = mydb.cursor()

        tablequery = 'CREATE TABLE users(First_name TEXT, Last_name TEXT, Email TEXT)'

        cur.execute(tablequery)

        print('table created!!')

    except:
        print('Could not create a table')

    mydb.close()

if __name__ == '__main__':
    main()