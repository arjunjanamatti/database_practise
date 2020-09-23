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

    ### UDATE METHOD#1
    cur = mydb.cursor()

    updatequery = 'UPDATE namelist SET first_name = "update_name" WHERE first_name = "Nayan" '

    cur.execute(operation = updatequery)

    ### UPDATE METHOD#2 using placeholder
    cur = mydb.cursor()

    updatequery_2 = 'UPDATE namelist SET first_name = %s WHERE first_name = %s '

    value = ('update_name_3', 'update_name_2')
    cur.execute(operation=updatequery_2, params = value)

    mydb.commit()

    mydb.close()


except Error as e:
    print('Error: {}'.format(e))
