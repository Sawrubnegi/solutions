import pymongo

# connect to MongoDB
client = pymongo.MongoClient("mongodb://<host>:<port>/")

# get the database
db = client["<database_name>"]

# get a collection
collection = db["<collection_name>"]

# insert a document
document = {"key": "value"}
collection.insert_one(document)

# query all documents
docs = list(collection.find({}))
print(docs)

# close the connection
client.close()
