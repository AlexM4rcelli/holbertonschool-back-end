#!/usr/bin/env python3
"""
    provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    collection = client.logs.nginx

    for mt in methods:
        print(f'\tmethod {mt}: {collection.count_documents({"method": mt})}')
    print(f'{collection.count_documents({"method": "GET", "path": "/status"})}'
          ' status check')