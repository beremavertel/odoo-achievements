# -*- coding: utf-8 --

import logging

from collections import defaultdict
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class ResUser(models.Model):
    _inherit = 'res.users'

    achievements = fields.One2many("achievement.achievement", "user", "Users achievement")

