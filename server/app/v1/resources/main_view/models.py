import json
from app import mongo
from flask_restplus import abort
from bson.json_util import dumps

class Queries:

    @staticmethod
    def get_all_stages():
        results = mongo.db.stages.find({}, {'_id': 0})

        return json.loads(dumps(results))

    @staticmethod
    def get_first_stage():
        result = mongo.db.stages.find_one({"name": "introduction"}, {'_id': 0})

        return json.loads(dumps(result))

    @staticmethod
    def get_name_stage(payload):
        result = mongo.db.stages.find_one({"name": payload["name"]}, {'_id': 0})

        return json.loads(dumps(result))
