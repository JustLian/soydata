from pymongo.mongo_client import MongoClient
from os.path import isfile
from json import load


def setup(host, port, username, password, db=None):
    global _host, _port, _username, _password, default_db
    _host = host
    _port = port
    _username = username
    _password = password
    if db:
        default_db = db
    else:
        default_db = None


def setup_from_cfg(fp: str):
    assert isfile(fp), "Can't find config file at {}".format(fp)
    with open(fp) as f:
        data = load(f)
    assert 'mongo' in data, "Can't find mongodb settings in file {}".format(fp)

    setup(**data['mongo'])
    if default_db:
        return connect().get_database(default_db)


def connect():
    return MongoClient(_host, _port, username=_username, password=_password)


def insert_document(collection, data):
    """
    Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id


def find_document(collection, elements, multiple=False):
    """
    Function to retrieve single or multiple documents from a provided
    Collection using a dictionary containing a document's elements.
    """
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)


def update_document(collection, query_elements, new_values):
    """ Function to update a single document in a collection."""
    collection.update_one(query_elements, {'$set': new_values})


def delete_document(collection, query):
    """ Function to delete a single document from a collection."""
    collection.delete_one(query)