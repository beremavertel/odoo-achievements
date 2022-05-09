# -*- coding: utf-8 --

import logging

from math import log10, floor
from collections import defaultdict
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class Achievement(models.Model):
    _name = 'achievement.achievement'
    _description = _('Achievement')

    model_name = fields.Char("Model name")
    number_created = fields.Integer("Number created")
    user = fields.Many2one("res.user", "User")

    toast_message = fields.Char()

    @api.depends("toast_message")
    def create_toast_message(self):
        _logger.warning(">>>>>>>>><<<<<<<<<")
        if self.toast_message:
            tm = {
                    "type": "ir.action.client",
                    "tag": "display_notification",
                    "params": {
                        "title": _("New achievement!"),
                        "message": self.toast_message,
                        "sticky": False,
                        }
                    }
            self.toast_message = False
            return tm

    @api.model
    def add_achievements(self, new_achievement_data):
        _logger.warning(new_achievement_data)
        current_user = self.env.uid
        achievement = self.env["achievement.achievement"].sudo()
        def create_search_domain(model_name):
            return [
                    ("model_name", "=", model_name),
                    ("user", "=", current_user),
                    ]

        for model_name, number_created in new_achievement_data.items():
            if model_name is None:
                continue
            _logger.warning(f"Adding {number_created} to model named '{model_name}')")
            if record := achievement.search(create_search_domain(model_name)):
                pre_count = record.number_created
                post_count = record.number_created = pre_count + number_created
            else:
                record = achievement.create({
                    "model_name": model_name,
                    "number_created": number_created,
                    "user": current_user
                    })
                pre_count = 0
                post_count = number_created

            if True or pre_count == 0 or floor(log10(pre_count)) != floor(log10(post_count)):
                record.toast_message = _("Congratulations, you just got a new achievement for creating {many} models of the type {model_name}").format(many=post_count, model_name=model_name)
            _logger.warning(f"{record.toast_message=}")
            _logger.warning(record.toast_message)




class BaseModel(models.AbstractModel):
    _inherit = "base"

    @api.model
    def create(self, vals):
        new_achievement_data = defaultdict(int)
        retval = super().create(vals)

        for created_object in retval.read():
            created_model = created_object.get("model")
            if created_model and created_model.startswith("achievement"):
                continue
            new_achievement_data[created_model] += 1

        if new_achievement_data:
            self.env["achievement.achievement"].add_achievements(new_achievement_data)

        return retval

