import logging

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from ..models.user import get_user

log = logging.getLogger(__name__)


@view_config(route_name='dashboard', permission='public',
             renderer="leaguenotifier:templates/dashboard.mako")
def dashboard(request):
	
    return {}