import mysql.connector
from mysql.connector.errors import Error

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

    cur = mydb.cursor()

    dropquery = 'DROP TABLE IF EXISTS namelist'

    cur.execute(operation = dropquery)

    print('Table dropped from the database')

except Error as e:
    print('Error: {}'.format(e))