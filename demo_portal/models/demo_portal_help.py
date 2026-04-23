# Copyright 2024 TechnoLibre
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class DemoPortalHelp(models.TransientModel):
    _name = "demo.portal.help"
    _description = "Demo Portal Tutorial"

    content_html = fields.Html(sanitize=False)

    @staticmethod
    def _get_help_html(is_fr=False):
        if is_fr:
            return """
<div style="font-family: sans-serif; max-width: 720px; margin: 0 auto;">

<h2>Constructeur de diagramme — Guide rapide</h2>
<p>Tout ce qu'il faut savoir pour créer votre premier diagramme de démonstration.</p>
<p><em>Note : les données affichées sont en lecture seule depuis le diagramme.
Modifiez-les via les menus Nœuds et Connexions.</em></p>

<h3>C'est quoi ce module ?</h3>
<p>Demo Portal est un module de démonstration qui illustre comment construire
un diagramme interactif dans Odoo. Il est composé de trois objets :</p>
<ul>
  <li><strong>Diagrammes</strong> — le conteneur principal (une bulle = un nœud)</li>
  <li><strong>Nœuds</strong> — les éléments affichés dans le diagramme</li>
  <li><strong>Connexions</strong> — les flèches qui relient les nœuds entre eux</li>
</ul>

<h3>Comment créer un diagramme ?</h3>
<ol>
  <li><strong>Menu → Nœuds</strong> — créez vos nœuds (chaque nœud = une bulle dans le diagramme)</li>
  <li><strong>Menu → Connexions</strong> — créez les connexions entre nœuds (Source → Destination)</li>
  <li><strong>Menu → Diagrammes</strong> — créez un diagramme et associez-lui les nœuds et connexions</li>
  <li>Depuis la fiche du diagramme, cliquez <strong>Voir le diagramme</strong> pour visualiser le résultat</li>
</ol>

<h3>Les boutons de la fiche Diagramme</h3>
<ul>
  <li><strong>Voir le diagramme</strong> — ouvre la vue diagramme interactive</li>
  <li><strong>Comment ça marche ?</strong> — ouvre ce guide (visible uniquement sur un diagramme sauvegardé)</li>
</ul>

<h3>Astuce</h3>
<p>Pour accéder à ce guide sans ouvrir de diagramme, utilisez le menu
<strong>Configuration → Guide rapide</strong>.</p>

</div>
"""
        else:
            return """
<div style="font-family: sans-serif; max-width: 720px; margin: 0 auto;">

<h2>Demo Portal — Quick Guide</h2>
<p>Everything you need to know to create your first demo diagram.</p>
<p><em>Note: data displayed in the diagram is read-only.
Edit it through the Nodes and Connections menus.</em></p>

<h3>What is this module?</h3>
<p>Demo Portal is a demonstration module that shows how to build an interactive
diagram in Odoo. It is made up of three objects:</p>
<ul>
  <li><strong>Diagrams</strong> — the main container (one bubble = one node)</li>
  <li><strong>Nodes</strong> — the elements displayed in the diagram</li>
  <li><strong>Connections</strong> — the arrows linking nodes together</li>
</ul>

<h3>How to create a diagram?</h3>
<ol>
  <li><strong>Menu → Nodes</strong> — create your nodes (each node = one bubble in the diagram)</li>
  <li><strong>Menu → Connections</strong> — create connections between nodes (Source → Destination)</li>
  <li><strong>Menu → Diagrams</strong> — create a diagram and associate nodes and connections to it</li>
  <li>From the diagram record, click <strong>View Diagram</strong> to see the result</li>
</ol>

<h3>Buttons on the Diagram form</h3>
<ul>
  <li><strong>View Diagram</strong> — opens the interactive diagram view</li>
  <li><strong>How does it work?</strong> — opens this guide (visible only on a saved diagram)</li>
</ul>

<h3>Tip</h3>
<p>To access this guide without opening a diagram, use the menu
<strong>Configuration → Quick Guide</strong>.</p>

</div>
"""
