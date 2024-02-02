from odoo import models, fields


class Genre(models.Model):
    _name = "game_dev.genre"
    _description = "Game Genre"

    name = fields.Char(required=True)
