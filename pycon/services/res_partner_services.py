# Copyright 2022-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo.addons.component.core import Component


class ResPartnerService(Component):
    _inherit = "base.rest.service"
    _name = "res.partner.service"
    _usage = "partner"
    _collection = "base.rest.pycon.public.services"
    _description = """
        All your res.partner are belong to us.\n
        No OCA community members were harmed in the making of this module.\n
        Made with ❤️ by Rapsodoo Italia, a Symphonie Prime Company, for
         Pycon Italia 2022\n
        https://www.rapsodoo.com - https://www.symphonieprime.com
    """
