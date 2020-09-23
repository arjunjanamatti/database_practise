import _sqlite3


users_tuples = (
    ('Aj', 'last_name', 'aj@gmail.com'),
('Bj', 'last_name', 'bj@gmail.com'),
('Cj', 'last_name', 'cj@gmail.com'),
('Dj', 'last_name', 'dj@gmail.com'),
('Ej', 'last_name', 'ej@gmail.com'),
('Fj', 'last_name', 'fj@gmail.com'),
)

mydb = _sqlite3.connect(database = 'namelist')

with mydb:
    cur = mydb.cursor()
    cur.executemany('INSERT INTO users VALUES (?,?,?)', users_tuples)

    print('Data added!!')

mydb.close()