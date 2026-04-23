from odoo import api, fields, models


class DemoModel3PortalDiagram(models.Model):
    _name = "demo.model_3.portal.diagram"
    _inherit = "portal.mixin"
    _description = "demo_model_3_portal_diagram"

    name = fields.Char()

    diagram_demo2_ids = fields.One2many(
        comodel_name="demo.model_2.portal",
        inverse_name="diagram_id",
        string="Connections",
    )

    diagram_demo_ids = fields.One2many(
        comodel_name="demo.model.portal",
        inverse_name="diagram_id",
        string="Nodes",
    )

    label_connections = fields.Char(compute="_compute_labels")
    label_nodes = fields.Char(compute="_compute_labels")

    @api.depends()
    def _compute_labels(self):
        IrField = self.env["ir.model.fields"]
        f_connections = IrField._get("demo.model_3.portal.diagram", "diagram_demo2_ids")
        f_nodes = IrField._get("demo.model_3.portal.diagram", "diagram_demo_ids")
        for rec in self:
            rec.label_connections = f_connections.field_description
            rec.label_nodes = f_nodes.field_description

    def action_open_help(self):
        lang = (self.env.lang or self.env.user.lang or "en_US").lower()
        is_fr = lang.startswith("fr")
        HelpModel = self.env["demo.portal.help"]
        content = HelpModel._get_help_html(is_fr)
        rec = HelpModel.create({"content_html": content})
        return {
            "type": "ir.actions.act_window",
            "name": "Comment ça marche ?" if is_fr else "How does the Demo Portal work?",
            "res_model": "demo.portal.help",
            "res_id": rec.id,
            "view_mode": "form",
            "target": "new",
            "views": [(False, "form")],
        }

    def action_open_diagram(self):
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "demo_portal.demo_model_3_portal_diagram_demo_model_3_portal_diagram_action_window"
        )
        action["res_id"] = self.id
        action["views"] = [(False, "diagram")]
        return action

    def _compute_access_url(self):
        # This is a comment need it for test, thanks
        super(DemoModel3PortalDiagram, self)._compute_access_url()
        for demo_model_3_portal_diagram in self:
            demo_model_3_portal_diagram.access_url = (
                "/my/demo_model_3_portal_diagram/%s"
                % demo_model_3_portal_diagram.id
            )
