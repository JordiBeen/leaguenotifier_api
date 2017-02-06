import logging
import transaction

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from ..lib.security import hash_password
from ..models import persist
from ..models.user import User, get_user


log = logging.getLogger(__name__)


@view_config(route_name='register_view', permission='public',
             renderer="leaguenotifier:templates/register.mako")
def register_view(request):
    
    return {}


@view_config(route_name='register_post', permission='public',
             renderer="json")
def register_post(request):

    post = request.POST
    username = post.get('username')
    password = post.get('password')
    email = post.get('email')

    # Fallback url will be login_view
    url = request.route_url('login_view')

    with transaction.manager:
        if get_user(username=username):
            request.session.flash('Username already taken.')
            url = request.route_url('register_view') 
        elif get_user(email=email):
            request.session.flash('Email already taken.')
            url = request.route_url('register_view') 
        else:
            u = User()
            u.username = username
            u.email = email
            u.password = hash_password(password)
            persist(u)
            request.session.flash('User registered successfully.')

    return HTTPFound(location=url)



