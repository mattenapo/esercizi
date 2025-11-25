import pymongo
import tornado.ioloop
import tornado.web
import json
from bson import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["publisher_db"]
publishers_collection = db["publishers"]
books_collection = db["books"]