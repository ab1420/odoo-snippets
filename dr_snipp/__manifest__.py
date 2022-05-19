# -*- coding: utf-8 -*-
# Copyright (c) 2019-Present Droggol. (<https://www.droggol.com/>)

{
    'name': 'Snippets',
    'description': 'Snippets',
    'summary': 'Snippets',
    'category': 'eCommerce',
    'author': 'Droggol Infotech Pvt. Ltd.',
    'license': 'OPL-1',
    'depends': [
        'website',
    ],
    'data': [
        'views/dr_login.xml',
        'views/dr_social.xml',
        'views/dr_effect.xml',
        'views/dr_card.xml',
        'views/dr_main.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'dr_snipp/static/src/scss/dr_style.scss',
            'dr_snipp/static/src/scss/dr_card_style.scss',
            'dr_snipp/static/js/dr_card_jquery.js',
        ],
        'web.assets_qweb': [
            'dr_snipp/static/src/xml/dr_card_js.xml',
        ]
    }
}
