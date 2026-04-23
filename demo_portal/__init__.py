# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

import json

from . import controllers, models


def post_init_hook(env):
    """Apply fr_CA translations for kanban inline labels."""
    _apply_kanban_translations(env)


def uninstall_hook(env):
    pass


def _apply_kanban_translations(env):
    kanban_translations = {
        "demo_portal.demo_model_portal_view_kanban": [
            ("Diagram: ", "Diagramme : "),
            ("Source: ", "Source : "),
            ("Destination: ", "Destination : "),
        ],
        "demo_portal.demo_model_2_portal_view_kanban": [
            ("Destination: ", "Destination : "),
            ("Source: ", "Source : "),
            ("Diagram: ", "Diagramme : "),
        ],
    }
    for xmlid, replacements in kanban_translations.items():
        view = env.ref(xmlid, raise_if_not_found=False)
        if not view:
            continue
        env.cr.execute(
            "SELECT arch_db FROM ir_ui_view WHERE id = %s", [view.id]
        )
        row = env.cr.fetchone()
        if not row:
            continue
        arch_dict = row[0] if isinstance(row[0], dict) else json.loads(row[0])
        en = arch_dict.get("en_US", "")
        fr = arch_dict.get("fr_CA", en)
        for src, dst in replacements:
            fr = fr.replace(src, dst)
        arch_dict["fr_CA"] = fr
        env.cr.execute(
            "UPDATE ir_ui_view SET arch_db = %s WHERE id = %s",
            [json.dumps(arch_dict), view.id],
        )
