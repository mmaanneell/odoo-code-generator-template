from odoo import _, api, fields, models


class DemoModel2Portal(models.Model):
    _name = "demo.model_2.portal"
    _inherit = ["mail.activity.mixin", "mail.thread", "portal.mixin"]
    _description = "demo_model_2_portal"

    name = fields.Char(tracking=True)

    demo_many2one_dst = fields.Many2one(
        comodel_name="demo.model.portal",
        string="Destination",
    )

    demo_many2one_src = fields.Many2one(
        comodel_name="demo.model.portal",
        string="Source",
    )

    diagram_id = fields.Many2one(
        comodel_name="demo.model_3.portal.diagram",
        string="Diagram",
    )

    label_diagram = fields.Char(compute="_compute_labels")
    label_source = fields.Char(compute="_compute_labels")
    label_destination = fields.Char(compute="_compute_labels")

    @api.depends()
    def _compute_labels(self):
        IrField = self.env["ir.model.fields"]
        f_diagram = IrField._get("demo.model_2.portal", "diagram_id")
        f_source = IrField._get("demo.model_2.portal", "demo_many2one_src")
        f_destination = IrField._get("demo.model_2.portal", "demo_many2one_dst")
        for rec in self:
            rec.label_diagram = f_diagram.field_description
            rec.label_source = f_source.field_description
            rec.label_destination = f_destination.field_description

    def _compute_access_url(self):
        super(DemoModel2Portal, self)._compute_access_url()
        for demo_model_2_portal in self:
            demo_model_2_portal.access_url = (
                "/my/demo_model_2_portal/%s" % demo_model_2_portal.id
            )
