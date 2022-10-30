from json import dump

from odoo import http
from odoo.http import request


class TeamController(http.Controller):
    @http.route(["/team_mates"], type="json", auth="public", website=True,)
    def get_all_team_mates(self):
        team_mates = request.env["res.partner"].sudo().search(
            [
                ("consent", "=", True)
            ])
        return {"teammates": [{
            "name": team_mate.name,
            "avatar": "/web/image/res.partner/{}/avatar_128".format(team_mate.id),
            "comment": team_mate.comment,
        } for team_mate in team_mates]}

    @http.route("/team_snippet", auth="public")
    def get_team_snippet(self):
        team_mates = request.env["res.partner"].sudo().search(
            [
                ("consent", "=", True)
            ])
        return  request.env['ir.binary']._get_image_stream_from(
                team_mates[0], 'avatar_1920'
            ).get_response()
