# -*- coding: utf-8 -*-
{
    'name': "openacademyDAM",

    'summary': """
        Modulo para clase de DAM""",

    'description': """
        Long description del modulo bla bla bla
    """,

    'author': "My Company DAM",
    'website': "http://www.danielcastelao.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '4.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/security.xml',
        #'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
