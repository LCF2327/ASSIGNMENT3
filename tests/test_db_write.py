from pymongo import MongoClient
import os

def test_database_write():
    #Test if a document can be inserted into the database.
    username = os.getenv('MONGODB_USERNAME')
    password = os.getenv('MONGODB_PASSWORD')
    uri = f"mongodb+srv://{username}:{password}@cluster0.jtnz2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    db = client.shop_db
    test_collection = db.test_collection

    # Insert a test document
    test_doc = {"name": "Test Product", "price": 10.99}
    insert_result = test_collection.insert_one(test_doc)
    inserted_doc = test_collection.find_one({"_id": insert_result.inserted_id})
    test_collection.delete_one({"_id": insert_result.inserted_id})
    client.close()
    
    assert inserted_doc is not None
    assert inserted_doc["name"] == "Test Product"
    assert inserted_doc["price"] == 10.99
