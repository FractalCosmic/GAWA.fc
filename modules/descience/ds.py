from pymongo import MongoClient
from bson.objectid import ObjectId

class ResearchRepository:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['descience']
        self.collection = self.db['research']

    def add_research(self, title, author, content, keywords):
        research = {
            "title": title,
            "author": author,
            "content": content,
            "keywords": keywords,
            "reviews": [],
            "score": 0
        }
        return str(self.collection.insert_one(research).inserted_id)

    def get_research(self, id):
        return self.collection.find_one({"_id": ObjectId(id)})

    def add_review(self, research_id, reviewer, comment, score):
        self.collection.update_one(
            {"_id": ObjectId(research_id)},
            {"$push": {"reviews": {"reviewer": reviewer, "comment": comment, "score": score}}}
        )
        self.update_score(research_id)

    def update_score(self, research_id):
        research = self.get_research(research_id)
        scores = [review['score'] for review in research['reviews']]
        avg_score = sum(scores) / len(scores) if scores else 0
        self.collection.update_one(
            {"_id": ObjectId(research_id)},
            {"$set": {"score": avg_score}}
        )
