from flask_restplus import Resource, Namespace
from flask_jwt_extended import jwt_required
from .serializers import queries, queries_payload
from .models import Queries
import pandas as pd
import json
from bson.json_util import dumps
from app.helpers.system_names import new_names


api = Namespace('queries', 'Queries Endpoint')


@api.route('/')
class QueriesAPI(Resource):
    # @jwt_required
    @api.marshal_list_with(queries)
    @api.expect(queries_payload)
    @api.doc(responses={
        200: 'Success',
        400: 'Bad Request',
    }, security=None)
    def post(self):
        """
        Get queries with filters
        """
        if Queries.get_queries_with_filters(payload=api.payload):
            response = Queries.get_queries_with_filters(payload=api.payload)

            return json.loads(dumps(response))

        api.abort(400, "Time data does not match format '%d/%m/%Y")


@api.route('/report')
class ReportAPI(Resource):
    # @jwt_required
    @api.expect(queries_payload)
    @api.doc(responses={
        200: 'Success',
    }, security=None)
    def post(self):
        """
        Process the result of queries
        """

        df_clean_data = pd.DataFrame(
            Queries.get_queries_with_filters(payload=api.payload)
        )

        if df_clean_data.empty:
            return None
        total_users = list(df_clean_data['assigned_to_email'].dropna().unique())

        df_people_analytics = pd.DataFrame(
            Queries.get_people_analitycs_with_filters(list_user_email=total_users)
        ).fillna(value='')

        montlhy_report = []
        for user_email in total_users:
            user_azure = df_clean_data[df_clean_data['assigned_to_email'] == user_email]
            user_people_analytics = df_people_analytics[df_people_analytics['email'] == user_email]

            if user_people_analytics.empty:
                continue

            total_user_tasks = len(user_azure[user_azure['work_item_type'] == 'user_story']) + \
                               len(user_azure[user_azure['work_item_type'] == 'spike']) + \
                               len(user_azure[user_azure['work_item_type'] == 'product_backlog'])
            total_user_bugs = len(user_azure[user_azure['work_item_type'] == 'bug'])

            total_systems = list(df_clean_data['area_path'].unique())
            for worked_system in total_systems:
                system_context = user_azure[user_azure['system'] == worked_system]

                if system_context.empty:
                    continue

                system_user_tasks = len(system_context[system_context['work_item_type'] == 'user_story']) + \
                                    len(system_context[system_context['work_item_type'] == 'spike']) + \
                                    len(system_context[system_context['work_item_type'] == 'product_backlog'])
                system_user_bugs = len(system_context[system_context['work_item_type'] == 'bug'])

                if total_user_tasks + total_user_bugs == 0:
                    percentage = 0
                else:
                    percentage = round(
                        ((system_user_tasks) / (total_user_tasks + total_user_bugs)) * 100
                        , 4)

                user_tasks = {
                    "name": user_people_analytics.get('name').to_string(index=False).strip(),
                    "company": user_people_analytics.get('company').to_string(index=False).strip(),
                    "cost_center": user_people_analytics.get('cost_center').to_string(index=False).strip(),
                    "registry": user_people_analytics.get('registry').to_string(index=False).strip(),
                    "cpf": user_people_analytics.get('cpf').to_string(index=False).strip(),
                    "role": user_people_analytics.get('role').to_string(index=False).strip(),
                    "admission_date": user_people_analytics.get('admission_date').to_string(index=False).strip(),
                    "email": user_people_analytics.get('email').to_string(index=False).strip(),
                    "system": new_names[worked_system],
                    "system_user_tasks": system_user_tasks,
                    "system_user_bugs": system_user_bugs,
                    "percentage": f'{percentage} %'
                }
                montlhy_report.append(user_tasks)

        return montlhy_report
