from app.v1 import api
from flask_restplus import fields


queries = api.model('Queries', {
    'work_item_id': fields.String(required=True, description='The Username'),
    'work_item_type': fields.String(description='User Email'),
    'work_item_state': fields.String(description='Work item state'),
    'work_item_closed_date': fields.String(description='Work item closed date'),
    'task_id': fields.String(description='Task id'),
    'task_type': fields.String(description='Task Type'),
    'task_state': fields.String(description='Task State'),
    'task_closed_date': fields.String(description='Task Closed Date'),
    'card_title': fields.String(description='Card Title'),
    'assigned_to': fields.String(description='Assigned to'),
    'assigned_to_email': fields.String(description='Assigned to email'),
    'created_by': fields.String(description='Created by'),
    'created_date': fields.String(description='Created date'),
    'changed_date': fields.String(description='Changed date'),
    'system': fields.String(description='System name'),
    'url': fields.String(description='Url'),
})

queries_payload = api.model('Queries Payload', {
    'filter_work_item_id': fields.List(fields.Integer(description='Filter')),
    'filter_work_item_type': fields.List(fields.String(description='Filter')),
    'filter_work_item_state': fields.List(fields.String(description='Filter')),
    'filter_work_item_closed_date': fields.String(description='Filter'),
    'filter_task_id': fields.List(fields.Integer(description='Filter')),
    'filter_task_type': fields.List(fields.String(description='Filter')),
    'filter_task_state': fields.List(fields.String(description='Filter')),
    'filter_task_closed_date': fields.String(description='Filter'),
    'filter_card_title': fields.List(fields.String(description='Filter')),
    'filter_assigned_to': fields.List(fields.String(description='Filter')),
    'filter_assigned_to_email': fields.List(fields.String(description='Filter')),
    'filter_created_by': fields.List(fields.String(description='Filter')),
    'filter_created_date': fields.String(description='Filter'),
    'filter_changed_date': fields.String(description='Filter'),
    'filter_system': fields.List(fields.String(description='Filter')),
    'filter_url': fields.List(fields.String(description='Filter')),
})

