import pymongo
import tornado.ioloop
import tornado.web
import json
from bson import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["publisher_db"]
publishers_collection = db["publishers"]
books_collection = db["books"]

class PublisherHandler(tornado.web.RequestHandler):
    def get(self, publisher_id = None):
        query = {}
        if publisher_id:
            query['_id'] = ObjectId(publisher_id)
        else:
            name = self.get_argument('name', None)
            country = self.get_argument('country', None)
            if name:
                query['name'] = name
            if country:
                query['country'] = country
        publishers = list(publishers_collection.find(query))
        for p in publishers:
            p['_id'] = str(p['_id'])
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(publishers))

    def post(self):
        data = json.loads(self.request.body)
        result = publishers_collection.insert_one(data)
        self.set_header("Content-Type", "application/json")
        self.write({"inserted_id": str(result.inserted_id)})

    def put(self, publisher_id):
        data = json.loads(self.request.body)
        publishers_collection.update_one({'_id': ObjectId(publisher_id)}, {'$set': data})
        self.write({"status": "updated"})

    def delete(self, publisher_id):
        publishers_collection.delete_one({'_id': ObjectId(publisher_id)})
        self.write({"status": "deleted"})

