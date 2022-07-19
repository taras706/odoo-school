from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = []
    _description = "Hospital Patient"
    _order = "id desc"

