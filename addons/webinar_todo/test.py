import toolz

objectRequest = {
	"data": [
		{
			"Odoo_Id": 0,
			"UOMPRICE": 422.0000,
			"pricelist_IdS": "22,27,31,15,60,52,56,64,68"
		},
		{
			"Odoo_Id": 0,
			"UOMPRICE": 422.0000,
			"pricelist_IdS": "70"
		},
		{
			"Odoo_Id": 1452,
			"UOMPRICE": 188.8600,
			"pricelist_IdS": "22,27,31,31,15,60,52,56,64,68"
		}
    ]}

#print(type(objectRequest['data'][1]))

for x in objectRequest:
    for k in objectRequest[x]:
       k['pricelist_IdS'] = k['pricelist_IdS'].split(',')

print(objectRequest)
       

