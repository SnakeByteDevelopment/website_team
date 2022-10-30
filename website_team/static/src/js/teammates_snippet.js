odoo.define("website_team.teammates", function (require) {
    var pw = require("web.public.widget");
    var rpc = require("web.rpc");
    var core = require("web.core");
    var QWeb = core.qweb;
    var TeamMates = pw.Widget.extend({
        selector: '.dynamic_snippet_teammates',
        start: function() {
            var self = this;
            rpc.query({
                route: "/team_mates",
                params: {},
            }).then(function (result) {

                self.$('.teammates').html(core.qweb.render("company_team_snippet_content", result))
            });
        },
    });
    pw.registry.dynamic_snippet_teammates = TeamMates;
    return TeamMates;
});