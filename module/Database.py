from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime
import certifi

# Load environment variables
load_dotenv()


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")

        self.client = MongoClient(self.mongo_uri, tlsCAFile=certifi.where())
        self.db = self.client.period_tracker_db

        # Check connection
        try:
            # Send a ping command to confirm successful connection
            self.client.admin.command("ping")
            print("MongoDB connection successful!")
        except Exception as e:
            print(f"Cannot connect to MongoDB: {e}")

    def save_data(self, collection_name, data):
        try:
            collection = self.db[collection_name]
            result = collection.insert_one(data)
            return str(result.inserted_id) if result.acknowledged else None
        except Exception as e:
            print(f"Error saving data: {e}")
            return None

    def save_many(self, collection_name, data_list):
        """
        Save multiple documents to a collection.

        Args:
            collection_name (str): Collection name
            data_list (list): List of dict documents to save

        Returns:
            list: List of inserted IDs or empty list on failure
        """
        try:
            collection = self.db[collection_name]
            for doc in data_list:
                doc["created_at"] = datetime.now()
            result = collection.insert_many(data_list)
            return [str(_id) for _id in result.inserted_ids]
        except Exception as e:
            print(f"Error saving multiple documents: {e}")
            return []

    def find_one(self, collection_name, query):
        """
        Find one document in collection

        Args:
            collection_name (str): Collection name
            query (dict): Query for searching

        Returns:
            dict: Found document or None
        """
        try:
            collection = self.db[collection_name]
            return collection.find_one(query)
        except Exception as e:
            print(f"Error finding data: {e}")
            return None

    def find_many(self, collection_name, query, limit=0, sort_by=None, sort_order=-1):
        """
        Find multiple documents in collection

        Args:
            collection_name (str): Collection name
            query (dict): Query for searching
            limit (int): Limit number of results
            sort_by (str): Field used for sorting
            sort_order (int): 1 for ascending, -1 for descending

        Returns:
            list: List of documents
        """
        try:
            collection = self.db[collection_name]
            if sort_by:
                return list(
                    collection.find(query).sort(sort_by, sort_order).limit(limit)
                )
            return list(collection.find(query).limit(limit))
        except Exception as e:
            print(f"Error finding data: {e}")
            return []

    def update_one(self, collection_name, query, update_data):
        """
        Update one document

        Args:
            collection_name (str): Collection name
            query (dict): Query to find document to update
            update_data (dict): Update data

        Returns:
            bool: True if successful, False if failed
        """
        try:
            collection = self.db[collection_name]
            # Add timestamp
            if "$set" not in update_data:
                update_data = {"$set": update_data}
            update_data["$set"]["updated_at"] = datetime.now()
            result = collection.update_one(query, update_data)
            return result.modified_count > 0
        except Exception as e:
            print(f"Error updating data: {e}")
            return False


db = Database()
