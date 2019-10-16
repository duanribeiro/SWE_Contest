import json
from app import mongo
from flask_restplus import abort
from bson.json_util import dumps
from datetime import datetime

class Queries:

    @staticmethod
    def get_queries_with_filters(payload):
        pipeline = []

        # Filtros do tipo LISTAS
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
        if payload.get("filter_system"):
            pipeline.append(
                {"$match": {"system": {"$lte": payload.get('filter_system')}}},
            )

        # Filtros do tipo DATAS
        try:
            for key in ['filter_created_date', 'filter_work_item_closed_date', 'filter_task_closed_date',
                        'filter_created_date']:
                if payload.get(key):
                    datetime.strptime(payload.get(key), "%d/%m/%Y")
        except:
            return None


        if payload.get("filter_created_date"):
            filter_created_date = datetime.strptime(payload.get("filter_created_date"), "%d/%m/%Y")
            pipeline.append(
                {"$match": {"created_date": {"$lte": filter_created_date}}}
            )
        if payload.get("filter_work_item_closed_date"):
            filter_work_item_closed_date = datetime.strptime(payload.get("filter_work_item_closed_date"), "%d/%m/%Y")
            pipeline.append(
                {"$match": {"work_item_closed_date": {"$lte": filter_work_item_closed_date}}}
            )
        if payload.get("filter_task_closed_date"):
            filter_task_closed_date = datetime.strptime(payload.get("filter_task_closed_date"), "%d/%m/%Y")
            pipeline.append(
                {"$match": {"task_closed_date": {"$lte": filter_task_closed_date}}}
            )
        if payload.get("filter_created_date"):
            filter_changed_date = datetime.strptime(payload.get("filter_changed_date"), "%d/%m/%Y")
            pipeline.append(
                {"$match": {"changed_date": {"$lte": filter_changed_date}}}
            )

        pipeline.append(
            {"$sort": {"assigned_to": 1}}
        )

        results = mongo.db.queries.aggregate(pipeline)
        return results


    @staticmethod
    def get_people_analitycs():
        results = mongo.db.people_analytics.find({}, {'_id': 0})

        return json.loads(dumps(results))

    @staticmethod
    def get_people_analitycs_with_filters(list_user_email):
        results = mongo.db.people_analytics.find({"email": {"$in": list_user_email}}, {'_id': 0}).sort('name', 1)

        return results
