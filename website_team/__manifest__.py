# -*- coding: utf-8 -*-
{
    'name': "Teammates snippet",

    'summary': """
        Dynamic snippet to show the team on your website""",

    'description': """
    """,

    'author': "Gert Pellin",
    'website': "https://snakebyte-development.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', "website"],

    # always loaded
    'data': [
        "views/res_partner_views.xml",
        "views/snippets/team_snippet.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            'website_team/static/src/scss/website_team.scss',
            'website_team/static/src/xml/teanm_snippet_teammate.xml',
            'website_team/static/src/js/teammates_snippet.js',
        ],
    },
}
