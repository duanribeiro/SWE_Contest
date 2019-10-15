from flask_restplus import Resource, Namespace
from flask_jwt_extended import jwt_required
from .serializers import queries, queries_payload
from .models import Queries

api = Namespace('queries', 'Queries Endpoint')


@api.route('/')
class QueriesAPI(Resource):

    # @jwt_required
    @api.marshal_list_with(queries)
    def get(self):
        """
        Get all queries
        """

        return Queries.get_all_queries()

    # @jwt_required
    @api.marshal_list_with(queries)
    @api.expect(queries_payload)
    def post(self):
        """
        Get queries with filters
        """

        return Queries.get_queries_with_filters(payload=api.payload)
