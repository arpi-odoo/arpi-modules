from odoo import models, fields


class Game(models.Model):
    _name = "game_dev.game"
    _description = "Video Game"

    name = fields.Char(required=True)
    description = fields.Char()
    image = fields.Image(max_width=512, max_height=512)

    genre_ids = fields.Many2many('game_dev.genre')
