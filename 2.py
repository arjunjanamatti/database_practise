import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main():
    'connect to the database'
    try:
        myclient = MongoClient()
        mydb = myclient['my_database']
        # collections is similar to tables in mongo dn

        my_collection = mydb['customers']
        my_dictionary = {'first_name': 'Gayathri',
                         'last_name': 'Arjun Janamatti'}

        my_collection.insert(doc_or_docs = my_dictionary)

        print('Data sent to the database')

    except ConnectionFailure:
        print('Failed to connect to mongoDB database')






if __name__ == '__main__':
    main()