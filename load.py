from pymongo import MongoClient
from config import ROOT_FOLDER, MONGO_URI, MONGO_DATABASE, MONGO_COLLECTION
from transform import get_fields
import csv
import os
import time

client = MongoClient(MONGO_URI)

database = client.get_database(MONGO_DATABASE)

collection = database.get_collection(MONGO_COLLECTION)

start = time.perf_counter()

for root, dirs, files in os.walk(os.path.join(ROOT_FOLDER, "csv")):
    for file in files:
        with open(os.path.join(root, file), 'r') as f:
            _csv_reader = csv.DictReader(f)
            collection.insert_many([get_fields(row, file) for row in _csv_reader])
            print(f"Loaded file {file}")


end = time.perf_counter()
print("Elapsed time: ", {end - start})
