#
url = 'http://localhost:8069'
db = 'odoo14'
username = 'andesarrollo@invertropoli.com' # Username (Email)
password = 'secret'  #Password (No la master, la password)

import xmlrpc.client, json, base64

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
output = common.version()

uid = common.authenticate(db, username, password, {})
print(output, uid)

#Example get Models
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
test = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])

print(test)