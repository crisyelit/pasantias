# -*- coding: utf-8 -*-
from odoo import fields, models

class Company(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.company model, by default partners are not
    # empresa
    razon_social_ids = fields.One2many('res.company','Empresa', string='Razon social de la Institucion',default='Razon social', traslate=True,  size=20, required='True', copy=True, help='Razon social de la Institucion')
    empresa_ids = fields.One2many('convenios', 'empresa_id',string="Empresa", readonly=True, required=True, copy=False, help='Empresa donde se ejecuta la pasantia')