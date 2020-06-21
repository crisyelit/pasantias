# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    instructor = fields.Boolean("Instructor", default=False)
    empresa_ids = fields.One2many('convenios', 'empresa_id',string="Empresa", readonly=True, required=True, copy=False, help='Empresa donde se ejecuta la pasantia')
    
