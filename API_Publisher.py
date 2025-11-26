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


class BookHandler(tornado.web.RequestHandler):
    def get(self, publisher_id=None, book_id=None):
        query = {}
        if publisher_id:
            query['publisher_id'] = ObjectId(publisher_id)
        if book_id:
            query['_id'] = ObjectId(book_id)
        title = self.get_argument('title', None)
        author = self.get_argument('author', None)
        genre = self.get_argument('genre', None)
        if title:
            query['title'] = title
        if author:
            query['author'] = author
        if genre:
            query['genre'] = genre

        cursor = books_collection.find(query)
        books = []
        for doc in cursor:
            doc['_id'] = str(doc['_id'])
            doc['publisher_id'] = str(doc['publisher_id'])
            books.append(doc)
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(books))

    def post(self, publisher_id=None):
        data = json.loads(self.request.body)
        if publisher_id:
            data['publisher_id'] = ObjectId(publisher_id)
        result = books_collection.insert_one(data)
        self.set_header("Content-Type", "application/json")
        self.write({"inserted_id": str(result.inserted_id)})

    def put(self, book_id):
        data = json.loads(self.request.body)
        books_collection.update_one({'_id': ObjectId(book_id)}, {'$set': data})
        self.write({"status": "updated"})

    def delete(self, book_id):
        books_collection.delete_one({'_id': ObjectId(book_id)})
        self.write({"status": "deleted"})


app = tornado.web.Application([
    (r"/publishers", PublisherHandler),
    (r"/publishers/([0-9a-fA-F]{24})", PublisherHandler),
    (r"/publishers/([0-9a-fA-F]{24})/books", BookHandler),
    (r"/publishers/([0-9a-fA-F]{24})/books/([0-9a-fA-F]{24})", BookHandler),
    (r"/books", BookHandler),
    (r"/books/([0-9a-fA-F]{24})", BookHandler),
])

if __name__ == "__main__":
    app.listen(8888)
    print("Server avviato su http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()