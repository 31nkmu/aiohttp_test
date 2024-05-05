from aiohttp.web import run_app
import click

from src.core.conf import settings
from src.core.registrar import register_app

app = register_app()


@click.command()
@click.option('--host', default=settings.HOST)
@click.option('--port', default=settings.PORT)
def main(host: str, port: int):
    run_app(
        app,
        port=port,
        host=host
    )


if __name__ == '__main__':
    main()
