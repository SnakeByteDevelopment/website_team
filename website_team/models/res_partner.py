from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    consent = fields.Boolean("Gives consent to be published on the site")
