# -*- coding: utf-8 -*-
{
    'name': "ITSM系统维护信息",

    'summary': """
        ITSM系统维护信息
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "ls",
    'website': "http://www.digitalchina.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'xc_addons/xc_itsm',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/itsm_security.xml',
        'security/ir.model.access.csv',
        # 'views/templates.xml',
        'views/business_systems_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
