import json
from app import mongo
from flask_restplus import abort
from bson.json_util import dumps
from bson.objectid import ObjectId
from app.helpers import encrypt_password
from datetime import datetime

class Queries:

    def __init__(self):
        pass

    @staticmethod
    def get_all_queries():

        return json.loads(
            dumps(
                mongo.db.queries.find().sort([('assigned_to', 1)])
            )
        )


    @staticmethod
    def get_queries_with_filters(payload):
        pipeline = []

        if payload.get("filter_work_item_id"):
            pipeline.append(
                {"$match": {"work_item_id": {"$in": payload.get('filter_work_item_id')}}},
            )
        if payload.get("filter_work_item_type"):
            pipeline.append(
                {"$match": {"work_item_type": {"$in": payload.get('filter_work_item_type')}}}
            )
        if payload.get("filter_work_item_state"):
            pipeline.append(
                {"$match": {"work_item_state": {"$in": payload.get('filter_work_item_state')}}}
            )
        if payload.get("filter_work_item_closed_date"):
            filter_work_item_closed_date = datetime.strptime(payload.get("filter_work_item_closed_date"), "%d/%m/%Y")
            pipeline.append(
                {"$match": {"work_item_closed_date": {"$lte": filter_work_item_closed_date}}}
            )
        if payload.get("filter_work_item_state"):
            pipeline.append(
                {"$match": {"task_id": {"$in": payload.get('filter_work_item_state')}}}
            )
        if payload.get("filter_task_type"):
            pipeline.append(
                {"$match": {"task_type": {"$in": payload.get('filter_task_type')}}}
            )
        if payload.get("filter_task_state"):
            pipeline.append(
                {"$match": {"task_state": {"$in": payload.get('filter_task_state')}}}
            )
        if payload.get("filter_task_closed_date"):
            filter_task_closed_date = datetime.strptime(payload.get("filter_task_closed_date"), "%d/%m/%Y")

            pipeline.append(
                {"$match": {"task_closed_date": {"$lte": filter_task_closed_date}}}
            )
        if payload.get("filter_assigned_to"):
            pipeline.append(
                {"$match": {"assigned_to": {"$in": payload.get('filter_assigned_to')}}}
            )
        if payload.get("filter_assigned_to_email"):
            pipeline.append(
                {"$match": {"assigned_to_email": {"$in": payload.get('filter_assigned_to_email')}}}
            )
        if payload.get("filter_created_by"):
            pipeline.append(
                {"$match": {"created_by": {"$in": payload.get('filter_created_by')}}}
            )
        if payload.get("filter_created_date"):
            filter_created_date = datetime.strptime(payload.get("filter_created_date"), "%d/%m/%Y")

            pipeline.append(
                {"$match": {"created_date": {"$lte": filter_created_date}}}
            )
        if payload.get("filter_created_date"):
            filter_changed_date = datetime.strptime(payload.get("filter_changed_date"), "%d/%m/%Y")

            pipeline.append(
                {"$match": {"changed_date": {"$lte": filter_changed_date}}}
            )
        if payload.get("filter_system"):
            pipeline.append(
                {"$match": {"system": {"$lte": payload.get('filter_system')}}},
            )

        results = mongo.db.queries.aggregate(pipeline)
        if results:
            return json.loads(dumps(results))
        return None
    #
    # @staticmethod
    # def insert_user(user):
    #     if mongo.db.users.find_one({'username': user.get('username')}):
    #         abort(409, 'User already exists')
    #
    #     user['password'] = encrypt_password(user.get('password', 'changeme'))
    #     if not mongo.db.users.insert_one(user).inserted_id:
    #         abort(422, 'Cannot create user')
    #     return json.loads(dumps(user))
    #
    # @classmethod
    # def update_user(cls, id, data):
    #     if not cls.get_user(id):
    #         abort(404, 'User not found')
    #
    #     if mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set': data}):
    #         return '', 204
    #     abort(422, 'No user updated')
    #
    # @classmethod
    # def delete_user(cls, id):
    #     if mongo.db.users.delete_one({'_id': ObjectId(id)}).deleted_count:
    #         return '', 204
    #     abort(404, 'User not found')
