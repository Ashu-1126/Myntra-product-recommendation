import json
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

def load_data_into_db():
    # Get MongoDB URI from environment variables
    mongo_uri = os.getenv("MONGO_URI")

    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client.get_default_database() # This is crucial for Flask-PyMongo integration

    # Define the collection
    products_collection = db.products
    
    # Check if the collection is already populated to avoid duplicate data
    if products_collection.count_documents({}) > 0:
        print("Database already contains data. Skipping data loading.")
        return

    # Path to the JSON data file
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'cleaned_myntra_dataset_frontend.json')
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # Insert the data into the products collection
            products_collection.insert_many(data)
            print(f"Successfully loaded {len(data)} products into the database.")
    except FileNotFoundError:
        print(f"Error: The file {json_path} was not found.")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
    finally:
        client.close()
