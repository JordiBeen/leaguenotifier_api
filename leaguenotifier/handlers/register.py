import logging
import transaction

from pyramid.view import view_config

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

    with transaction.manager:
        u = get_user(username=username)
        if not u:
            u = User()
            u.username = username
            u.email = email
            u.password = hash_password(password)

            persist(u)

    return {
        "test": "test"
    }


