import _sqlite3
from collections import defaultdict

mydb = _sqlite3.connect(database = 'namelist')

new_dict = defaultdict(list)
with mydb:
    cur = mydb.cursor()
    selectquery = 'SELECT * FROM users'

    cur.execute(selectquery)

    results = cur.fetchall()

    for row in results:
        new_dict['first_name'].append(row[0])
        new_dict['last_name'].append(row[1])
        new_dict['email'].append(row[2])

mydb.close()

print(new_dict)