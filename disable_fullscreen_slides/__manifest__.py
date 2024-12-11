# Copyright 2024 Elabore ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "disable_fullscreen_slides",
    "version": "16.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Elabore",
    "license": "AGPL-3",
    "category": "Website",
    "summary": "disables full-screen video opening",
    # any module necessary for this one to work correctly
    "depends": [
        "base","website_slides","web",
    ],
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        # "security/security.xml",
        # "security/ir.model.access.csv",
        # "views/menu.xml",
        # "data/data.xml",
    ],
    'assets': {
        'web.assets_frontend': [
            'disable_fullscreen_slides/static/src/js/slides_course_slides_list.js',
        ],
       },
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}