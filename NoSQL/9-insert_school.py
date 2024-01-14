#!/usr/bin/env python3
"""
    inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in the MongoDB collection based on kwargs."""

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
