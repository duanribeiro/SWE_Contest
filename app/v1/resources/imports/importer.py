from flask_restplus import Resource, Namespace
from flask_jwt_extended import jwt_required
from .models import Imports
import pandas as pd
from dateutil.parser import parse
from datetime import date

api = Namespace('imports', 'Imports Endpoint')


@api.route('/people_analytics')
class PeopleAnalyticsAPI(Resource):
    # @jwt_required
    @api.doc(responses={
        200: "Success",
        400: "Missing required columns on excel file",
        503: "Can't insert on mongo database"
    }, security=None)
    def post(self):
        """
        Import the people analytics excel file.
        """
        df_people_analytics = pd.read_excel('static_files/people_analytics.xlsx')

        response = Imports.insert_df_people_analytics(df_people_analytics)
        if response['status_code'] != 200:
            api.abort(response['status_code'], response['message'])

        return response['message']


