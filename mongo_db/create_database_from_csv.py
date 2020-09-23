import pandas as pd
import pymongo
from pymongo import MongoClient
import _json

class mongo_db(object):

    def __init__(self, dbNAme = None, collection_name = None):
        self.dbName = dbNAme
        self.collection_name = collection_name

        self.client = MongoClient()
        self.DB = self.client[self.dbName]
        self.collection = self.DB[self.collection_name]


    def insert_data(self, path = None):
        df = pd.read_csv(path)
        data = df.to_dict('records')

        self.collection.insert_many(documents = data,ordered = False)

        print('CSV exported to mongo DB database')


if __name__ == '__main__':
    mongoDB = mongo_db(dbNAme = 'csv_dataset', collection_name = 'melbourne_house_data')
    mongoDB.insert_data(path = 'melb_data.csv')

