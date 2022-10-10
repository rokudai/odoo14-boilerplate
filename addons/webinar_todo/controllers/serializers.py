from odoo.http import Response
from odoo.tools import date_utils
import json

def json_response(self, result=None, error=None):
  if error is not None:
      response = error
  if result is not None:
      response = result
  
  mime = 'application/json'
  body = json.dumps(response, default=date_utils.json_default)
  return Response(body, status=error and error.pop('http_status', 200) or 200,
    headers=[('Content-Type', mime), ('Content-Length', len(body))])