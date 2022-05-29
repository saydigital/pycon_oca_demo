# Copyright 2022-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo.addons.base_rest import restapi
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

    @restapi.method(
        [(["/<int:id>"], "GET")],
        auth="public",
    )
    def get_partner_by_id(self, id):
        """
        Get partner information
        """
        partner = self.env["res.partner"].browse(id)
        return self._to_json(partner)

    @restapi.method(
        [(["/"], "GET")],
        input_param=restapi.CerberusValidator("_validator_search_partners"),
        auth="public",
    )
    def search_partners(self, name):
        """
        Search partners by name
        """
        partner_obj = self.env["res.partner"]
        partners = partner_obj.browse(
            [p[0] for p in partner_obj.name_search(name)]
        )
        return {
            "count": len(partners),
            "rows": [self._to_json(p) for p in partners]
        }

    def _validator_search_partners(self):
        return {
            "name": {
                "type": "string",
                "nullable": False,
                "required": True
            }
        }

    def _to_json(self, partner):
        """
        Private Helper method to convert a partner record to a Json
        serializable dict
        """
        res = {
            "id": partner.id,
            "name": partner.name,
            "street": partner.street,
            "zip": partner.zip,
            "city": partner.city,
            "phone": partner.phone,
        }
        if partner.country_id:
            res["country"] = {
                "id": partner.country_id.id,
                "name": partner.country_id.name,
            }
        if partner.state_id:
            res["state"] = {
                "id": partner.state_id.id,
                "name": partner.state_id.name
            }

        return res
