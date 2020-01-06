from flask import Blueprint
from flask_restplus import Api

v1_blueprint = Blueprint('v1', __name__, url_prefix='/api/v1')


api = Api(v1_blueprint,
          doc='/docs',
          title='SWE Contest Documentation',
          version='1.0',
          description='Flask RESTful API')

from .resources.main_view.main import api as main_api

api.add_namespace(main_api)

