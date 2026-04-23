from odoo import api, fields, models


class DemoModelPortal(models.Model):
    _name = "demo.model.portal"
    _inherit = ["mail.activity.mixin", "mail.thread", "portal.mixin"]
    _description = "demo_model_portal"

    name = fields.Char()

    label_diagram = fields.Char(compute="_compute_labels")
    label_source = fields.Char(compute="_compute_labels")
    label_destination = fields.Char(compute="_compute_labels")

    @api.depends()
    def _compute_labels(self):
        IrField = self.env["ir.model.fields"]
        f_diagram = IrField._get("demo.model.portal", "diagram_id")
        f_source = IrField._get("demo.model.portal", "demo_one2many_dst")
        f_destination = IrField._get("demo.model.portal", "demo_one2many_src")
        for rec in self:
            rec.label_diagram = f_diagram.field_description
            rec.label_source = f_source.field_description
            rec.label_destination = f_destination.field_description

    demo_binary = fields.Binary(string="Binary demo")

    demo_binary_image = fields.Binary(string="Binary image demo")

    demo_boolean = fields.Boolean(string="Boolean demo")

    demo_char = fields.Char(
        string="Char demo",
        tracking=True,
    )

    demo_date = fields.Date(string="Date demo")

    demo_date_time = fields.Datetime(string="Datetime demo")

    demo_external_link = fields.Char(string="External link demo")

    demo_float = fields.Float(string="Float demo")

    demo_float_time = fields.Float(string="Float time demo")

    demo_html = fields.Html(string="HTML demo")

    demo_integer = fields.Integer(string="Integer demo")

    demo_many2many = fields.Many2many(
        comodel_name="demo.model_2.portal",
        string="Many2many demo",
    )

    demo_one2many_dst = fields.One2many(
        comodel_name="demo.model_2.portal",
        inverse_name="demo_many2one_dst",
        string="Source",
    )

    demo_one2many_src = fields.One2many(
        comodel_name="demo.model_2.portal",
        inverse_name="demo_many2one_src",
        string="Destination",
    )

    demo_selection = fields.Selection(
        selection=[
            ("test1", "Test 1"),
            ("test2", "Test 2"),
            ("test3", "Test 3"),
        ],
        string="Selection demo",
    )

    demo_text = fields.Text(string="Text demo")

    diagram_id = fields.Many2one(
        comodel_name="demo.model_3.portal.diagram",
        string="Diagram",
    )

    xpos = fields.Integer(
        string="Diagram position x",
        default=50,
    )

    ypos = fields.Integer(
        string="Diagram position y",
        default=50,
    )

    def _compute_access_url(self):
        # This is a comment need it for test, thanks
        super(DemoModelPortal, self)._compute_access_url()
        for demo_model_portal in self:
            demo_model_portal.access_url = (
                "/my/demo_model_portal/%s" % demo_model_portal.id
            )
