"""
Routes module to handle request urls
"""
from api.views.redflag_views import FlagViews
from api.views.auth_views import UserView


class Routes:
    """
    Class to generate urls
    """
    @staticmethod
    def generate(app):

        app.add_url_rule('/api/v2/redflags/', view_func=FlagViews.as_view('create_redflag'),
                         methods=['POST'], strict_slashes=False)

        app.add_url_rule('/api/v2/redflags/', view_func=FlagViews.as_view('get_all_redflags'),
                         methods=['GET'], strict_slashes=False)

        app.add_url_rule('/api/v2/redflags/<int:flag_id>', view_func=FlagViews.as_view('get_all_specific_redflag'),
                         methods=['GET'], strict_slashes=False)

        app.add_url_rule('/api/v2/redflags/<int:flag_id>',
                         view_func=FlagViews.as_view('edit_comment'),
                         methods=['PUT'], strict_slashes=False)

        app.add_url_rule('/api/v2/redflags/<int:flag_id>',
                         view_func=FlagViews.as_view('delete_redflag'),
                         methods=['DELETE'], strict_slashes=False)

        app.add_url_rule('/api/auth/user/', view_func=UserView.as_view('create_user'),
                         methods=['POST'], strict_slashes=False)

        app.add_url_rule('/api/auth/user/', view_func=UserView.as_view('Login_user'),
                         methods=['GET'], strict_slashes=False)


