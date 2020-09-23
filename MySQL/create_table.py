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

    ### CREATION OF TABLE
    cur = mydb.cursor()

    cur.execute(' DROP TABLE IF EXISTS namelist')

    sqlquery = '''
    CREATE TABLE namelist(
    First_name CHAR(20) NOT NULL,
    Last_name CHAR(30) NOT NULL,
    Email CHAR(45) NOT NULL
    )
    '''

    cur.execute(sqlquery)

    print('Table created in database!')

    mydb.close()

except Error as e:
    print('Error: {}'.format(e))