from odoo import models, fields, api

class ResPartner(models.Model):
    """
    about name_get and display name:
    * in this model name_get and name_search are re-defined so we overwrite
    them
    * we add display_name to replace name field use, we add
     with search funcion. This field is used then for name_get and name_search


    Acccoding this https://www.odoo.com/es_ES/forum/ayuda-1/question/
    how-to-override-name-get-method-in-new-api-61228
    we should modify name_get, we do that by creating a helper display_name
    field and also overwriting name_get to use it
    """
    _inherit = "res.partner"

    @api.multi
    @api.depends(
        'name', 'parent_id')
    def _get_contact_name(self, partner, name):
        return "%s, %s" % (name , partner.commercial_company_name or partner.parent_id.name)
        """
        We overwrite default name_get function to use document_number if
        available
        """