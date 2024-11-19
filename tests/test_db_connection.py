from pymongo import MongoClient
import os

def test_database_connection():
    #Test if the MongoDB connection is successful using the ping command
    username = os.getenv('MONGODB_USERNAME')
    password = os.getenv('MONGODB_PASSWORD')
    uri = f"mongodb+srv://c0917813:wtar4F6O9iuSjdY3@cluster0.jtnz2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    
    try:
        client.admin.command('ping')
        connection_successful = True
    except Exception:
        connection_successful = False
    finally:
        client.close()
    
    assert connection_successful
