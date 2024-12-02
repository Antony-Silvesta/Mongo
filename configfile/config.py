import os
from pymongo import MongoClient

# Get MongoDB URI and DB_NAME from environment variables
mongo_uri = os.getenv('MONGO_URI', "mongodb://127.0.0.1:27017/")  # Default to localhost if MONGO_URI is not set
db_name = os.getenv('DB_NAME', "sampleupload")  # Default database name to 'sampleupload'

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[db_name]  # Specify the database using the db_name variable

# List collections in the database
collections = db.list_collection_names()
print('Collections in the database:', collections)

# Close the MongoDB connection
client.close()
