# -*- coding: utf-8 -*-
{
    'name': "tcc_noticias (5)",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/groups.xml',
        'security/group_tcc_consejo/ir.model.access.csv',
        'security/group_tcc_residentes/ir.model.access.csv',
        'security/group_tcc_vocero/ir.model.access.csv',
        'security/public/ir.model.access.csv',
        'templates.xml',
        'views/noticias_views.xml',        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}