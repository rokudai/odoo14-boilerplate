from odoo import http
from odoo.http import request

class SyncPrices(http.Controller):
    @http.route('/helloworld', auth='public', website=True)
    def contacto(self, **kw):
        return f"Hola mundo {request.params['nombre']}"