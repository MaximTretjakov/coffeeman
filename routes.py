from view import index


def setup_routes(app):
    app.router.add_post('/', index)
