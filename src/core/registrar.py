from aiohttp.web import Application

from src.common.log import default_logger
from src.routers import routers

logger = default_logger.getChild(__name__)


def register_app() -> Application:
    app = Application()

    register_router(app)

    logger.info('Aiohttp server starting')
    return app


def register_router(app: Application):
    for route in routers:
        app.add_routes(route)
