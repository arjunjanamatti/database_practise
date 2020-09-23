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

    ### DELETE METHOD#1
    cur = mydb.cursor()

    deletequery = 'DELETE FROM namelist WHERE first_name = "gayathri"'

    cur.execute(operation = deletequery)

    print('Deleted the deletequery')

    mydb.commit()


    ### DELETE METHOD#2 using placeholder
    cur = mydb.cursor()

    deletequery_2 = 'DELETE FROM namelist WHERE first_name = %s '

    value = ('nayan',)

    cur.execute(operation = deletequery_2,
                params = value)

    print('Deleted the deletequery_2')

    mydb.commit()

    mydb.close()

except Error as e:
    print('Error: {}'.format(e))