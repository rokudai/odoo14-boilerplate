from urllib import response
from odoo import http, exceptions
from odoo.http import request, JsonRequest
from .serializers import json_response

class SyncPrices(http.Controller):
    
    
    @http.route(['/syncPrices'], auth='public', type='json', methods=['POST'])
    def contacto(self, **kw):
        response_data = request.jsonrequest
        
        format_data = self.mapToDataForItemList(response_data)
        return format_data
        
        #return data
        
    def mapToDataForItemList(self, objectRequestData):
        for indexRequestData in objectRequestData:
            for indexDictData in objectRequestData[indexRequestData]:
                indexDictData['pricelist_IdS'] = indexDictData['pricelist_IdS'].split(',')
        
        return objectRequestData