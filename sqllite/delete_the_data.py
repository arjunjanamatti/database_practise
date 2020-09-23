import _sqlite3


mydb = _sqlite3.connect(database = 'namelist')

with mydb:
    cur = mydb.cursor()

    name = 'update_name_placeholder'

    cur.execute('DELETE FROM users WHERE First_name = ?', (name,))

    mydb.commit()

    print('Data deleted!!!')

    cur = mydb.cursor()

    selectquery = 'SELECT * FROM users'

    cur.execute(selectquery)

    results = cur.fetchall()
    print('Original data: ')
    for row in results:
        print(row)
