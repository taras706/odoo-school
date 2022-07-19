from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = []
    _description = "Hospital Doctor"
    _rec_name = 'doctor_name'