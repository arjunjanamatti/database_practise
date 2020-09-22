import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from collections import defaultdict


def main():
    'connect to the database'
    try:
        myclient = MongoClient()
        mydb = myclient['my_database']
        # collections is similar to tables in mongo dn

        my_collection = mydb['customers']
        my_dictionary = {'first_name': 'Gayathri',
                         'last_name': 'Arjun Janamatti'}

        my_collection.insert(doc_or_docs=my_dictionary)

        print('Data sent to the database')

    except ConnectionFailure:
        print('Failed to connect to mongoDB database')


def get_data():
    try:
        myclient = MongoClient()
        mydb = myclient['my_database']
        # collections is similar to tables in mongo dn

        my_collection = mydb['customers']

        ### Find first data in row
        first_data = my_collection.find_one()
        print(' First data in the database: ', first_data)

        ### Find specific data
        specific_data = my_collection.find_one({'first_name': 'Ayan'})
        print(' Specific data in the database: ', specific_data)

        ### Find all the data
        print()
        print('Entire dataset: ')
        list_data = my_collection.find()
        for i in list_data:
            print(i)

        try_list = defaultdict(list)
        list_data = my_collection.find()

        for j in list_data:
            for k in j.keys():
                try_list[k].append(j[k])
            # try_list[j] .append(list_data[j])

        print(try_list)


    except ConnectionFailure:
        print('Failed to connect to mongo DB database')


if __name__ == '__main__':
    # main()
    get_data()