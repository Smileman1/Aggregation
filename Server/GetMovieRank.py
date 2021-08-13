from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbhwanE

target_point = db.movies.find_one({"title":"주전장"})["point"]
same_movie = list(db.movies.find({"point":target_point},{"_id":False}))

for same in same_movie:
    print(same["title"])