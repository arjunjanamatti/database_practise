import _sqlite3


mydb = _sqlite3.connect(database = 'namelist')

with mydb:
    cur = mydb.cursor()

    selectquery = 'SELECT * FROM users'

    cur.execute(selectquery)

    results = cur.fetchall()
    print('Original data: ')
    for row in results:
        print(row)

    cur = mydb.cursor()

    updatequery = 'UPDATE users SET first_name = "update_name" WHERE first_name = "Cj"'

    cur.execute(updatequery)

    cur = mydb.cursor()

    selectquery = 'SELECT * FROM users'

    cur.execute(selectquery)

    results = cur.fetchall()
    print()
    print('After updating data: ')
    for row in results:
        print(row)

    cur = mydb.cursor()
    user_change = 'update_name_placeholder'
    origin_name = 'update_name'

    cur.execute('UPDATE users SET first_name = ? WHERE First_name = ? ', (user_change, origin_name))
    cur = mydb.cursor()

    selectquery_2 = 'SELECT * FROM users'

    cur.execute(selectquery_2)

    results = cur.fetchall()
    print()
    print('After updating data: ')
    for row in results:
        print(row)

mydb.close()




