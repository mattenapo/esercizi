import asyncio
from pymongo import AsyncMongoClient

client = AsyncMongoClient("mongodb://localhost:27017")

db = client["publisher_db"]
publishers_collection = db["publishers"]
books_collection = db["books"]
async def doc():
    pub=await publishers_collection.insert_many([{
    "name": "Einaudi",
    "founded_year": 1933,
    "country": "Italia"
  },
  {
    "name": "Penguin Random House",
    "founded_year": 2013,
    "country": "USA"
  },
  {
    "name": "Mondadori",
    "founded_year": 1907,
    "country": "Italia"
  },
  {
    "name": "HarperCollins",
    "founded_year": 1989,
    "country": "USA"
  },
  {
    "name": "Feltrinelli",
    "founded_year": 1954,
    "country": "Italia"
  }])


    pub_id = pub.inserted_ids
    await books_collection.insert_many([{
    "title": "Il barone rampante",
    "author": "Italo Calvino",
    "genre": "Romanzo",
    "year": 1957,
    "publisher_id": pub_id[0]
    },
  {
    "title": "Se una notte d'inverno un viaggiatore",
    "author": "Italo Calvino",
    "genre": "Romanzo",
    "year": 1979,
    "publisher_id": pub_id[0]
  },
  {
    "title": "Il nome della rosa",
    "author": "Umberto Eco",
    "genre": "Giallo",
    "year": 1980,
    "publisher_id": pub_id[0]
  },
  {
    "title": "Il codice da Vinci",
    "author": "Dan Brown",
    "genre": "Giallo",
    "year": 2003,
    "publisher_id": pub_id[1]
  },
  {
    "title": "Harry Potter e la pietra filosofale",
    "author": "J.K. Rowling",
    "genre": "Fantasy",
    "year": 1997,
    "publisher_id": pub_id[1]
  },
  {
    "title": "Il signore degli anelli",
    "author": "J.R.R. Tolkien",
    "genre": "Fantasy",
    "year": 1954,
    "publisher_id": pub_id[1]
  },
  {
    "title": "1984",
    "author": "George Orwell",
    "genre": "Romanzo",
    "year": 1949,
    "publisher_id": pub_id[2]
  },
  {
    "title": "Hunger Games",
    "author": "Suzanne Collins",
    "genre": "Fantasy",
    "year": 2008,
    "publisher_id": pub_id[2]
  },
  {
    "title": "La ragazza del treno",
    "author": "Paula Hawkins",
    "genre": "Giallo",
    "year": 2015,
    "publisher_id": pub_id[3]
  },
  {
    "title": "Harry Potter e il prigioniero di Azkaban",
    "author": "J.K. Rowling",
    "genre": "Fantasy",
    "year": 1999,
    "publisher_id": pub_id[3]
  },
  {
    "title": "Il piccolo principe",
    "author": "Antoine de Saint-Exupéry",
    "genre": "Romanzo",
    "year": 1943,
    "publisher_id": pub_id[3]
  },
  {
    "title": "Il vecchio e il mare",
    "author": "Ernest Hemingway",
    "genre": "Romanzo",
    "year": 1952,
    "publisher_id": pub_id[3]
  },
  {
    "title": "Sostiene Pereira",
    "author": "Antonio Tabucchi",
    "genre": "Romanzo",
    "year": 1994,
    "publisher_id": pub_id[4]
  },
  {
    "title": "La ragazza del treno",
    "author": "Paula Hawkins",
    "genre": "Giallo",
    "year": 2015,
    "publisher_id": pub_id[4]
  },
  {
    "title": "Cecità",
    "author": "José Saramago",
    "genre": "Romanzo",
    "year": 1995,
    "publisher_id": pub_id[4]
  }])

asyncio.run(doc())