import logging

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget

from ..lib.security import check_password

from ..models.user import get_user

log = logging.getLogger(__name__)


@view_config(route_name='login_view', permission='public',
             renderer="leaguenotifier:templates/index.mako")
def login_view(request):
    
    return {}

@view_config(route_name='login_post', permission='public',
             renderer="json")
def login_post(request):

    post = request.POST
    username = post.get('username')
    password = post.get('password')

    # Fallback url will be login_view with an error message
    url = request.route_url('login_view')
    headers=None

    user = get_user(username=username)
    if user:
        if check_password(password, user.password):
            headers = remember(request, user.id)
            url = request.route_url('dashboard')
        else:
            request.session.flash('Password not correct.')
    else:
        request.session.flash('User not found.')

    
    return HTTPFound(location=url, headers=headers)
