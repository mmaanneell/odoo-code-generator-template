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

    def _compute_access_url(self):
        # This is a comment need it for test, thanks
        super(DemoModel3PortalDiagram, self)._compute_access_url()
        for demo_model_3_portal_diagram in self:
            demo_model_3_portal_diagram.access_url = (
                "/my/demo_model_3_portal_diagram/%s"
                % demo_model_3_portal_diagram.id
            )
