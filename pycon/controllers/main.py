# Copyright 2022-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo.addons.base_rest.controllers import main


class BaseRestPyconPublicApiController(main.RestController):
    _root_path = "/pycon/public/"
    _collection_name = "base.rest.pycon.public.services"
    _default_auth = "public"
