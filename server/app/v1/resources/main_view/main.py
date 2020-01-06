from flask_restplus import Resource, Namespace
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity, get_jwt_claims
from app import mongo, jwt
from .serializers import login, full_token, acc_token
from .models import Queries

api = Namespace('', 'Main API')


@api.route('/game')
class Game(Resource):

    @api.doc(responses={
        200: 'Success',
    }, security=None)
    def post(self):
        """
        Return all stages
        """
        return Queries.get_name_stage(api.payload)
