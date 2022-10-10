from select import select
from odoo import models, fields

class Todo(models.Model):
    _name = "nombre.modulo"
    
    name = fields.Char("name")
    status = fields.Selection(selection=[('Prueba uno', 'Prueba uno'), ])