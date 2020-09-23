import mysql.connector
from mysql.connector.errors import Error
from collections import defaultdict

databse_name = 'practise_db'
user_name = 'aj'
password = 'italia123'
host_address = 'localhost'

try:
    ### CONNECT TO THE DATABASE
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = user_name,
        passwd = password,
        database = databse_name
    )

    print('Successfully connected to database: {}'.format(mydb))

    ### SELECT DATA
    cur = mydb.cursor()

    selectquery = 'SELECT * FROM namelist'

    cur.execute(selectquery)

    results = cur.fetchall()

    new_dict = defaultdict(list)

    for row in results:
        new_dict['first_name'].append(row[0])
        new_dict['last_name'].append(row[1])
        new_dict['email'].append(row[2])


    print(new_dict)



except Error as e:
    print('Error: {}'.format(e))

