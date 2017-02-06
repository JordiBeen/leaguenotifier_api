def setup_routes(config):
    # Home / Login
    config.add_route('login_view', '/')

    # Login
    config.add_route('login_post',
                     '/login',
                     request_method='POST')

    # Register
    config.add_route('register_view',
                     '/register',
                     request_method='GET')
    config.add_route('register_post',
                     '/register',
                     request_method='POST')

    # Dashboard
    config.add_route('dashboard',
                     '/dashboard',
                     request_method='GET')
