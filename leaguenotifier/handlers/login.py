import logging

from pyramid.view import view_config

from ..models.user import get_user

log = logging.getLogger(__name__)


@view_config(route_name='login_view', permission='public',
             renderer="leaguenotifier:templates/index.mako")
def login_view(request):
	
    return {}
