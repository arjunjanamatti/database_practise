import sys
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main():
    'connect to the database'
    try:
        c = MongoClient(host = 'localhost', port = 27017)
        print('Connect to mongoDB')
    except ConnectionFailure:
        print('Cannot connect to mongoDB')

main()