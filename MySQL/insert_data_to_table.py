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

    ### ADDING DATA TO THE TABLE METHOD# 1
    cur = mydb.cursor()

    insertquery = '''
    INSERT INTO namelist(First_name, Last_name, Email) VALUES ('nayan', 'no_name', 'nayan@gmail.com')
    '''

    cur.execute(insertquery)

    mydb.commit()

    ### ADDING DATA TO THE TABLE METHOD# 2
    cur = mydb.cursor()
    insertquery_2 = '''
        INSERT INTO namelist(First_name, Last_name, Email) VALUES (%s, %s, %s)
    '''

    value = ('gayathri', 'no_name', 'gayathri@gmail.com')

    cur.execute(insertquery_2, value)

    mydb.commit()


    mydb.close()

except Error as e:
    print('Error: {}'.format(e))