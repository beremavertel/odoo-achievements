# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) {year} {company} (<{mail}>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
#
# https://www.odoo.com/documentation/14.0/reference/module.html
#
{
    'name': 'Achievement',
    'version': '14.0.0.0.0',
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.odoo.com""",
    'category': '',
    'description': """
        Long description of module's purpose
    """,
    'author': 'Emanuel Bergsten',
#    'website': 'https://vertel.se/apps/odoo-',
    'images': [
        'static/description/banner.png'
        ], # 560x280
    'license': 'AGPL-3',
    'depends': ['base'],
     #"external_dependencies": {
     #   "bin": ["openssl",],
     #   "python": ["acme_tiny", "IPy",],
     #},
    'data': [
        'views/res_user.xml',
        'views/achievement.xml',
        'security/ir.model.access.csv',
        ],
    'demo': [],
    'application': False,
    'installable': True,
    'auto_install': False,
    #"post_init_hook": "post_init_hook",
}
