import logging
from aiohttp import web

from routes import setup_routes
from db import init_pg, close_pg
from config import get_config


def main():
    app = web.Application()
    app['config'] = get_config()
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    setup_routes(app)
    web.run_app(app, host=app['config']['host'], port=app['config']['port'])


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
