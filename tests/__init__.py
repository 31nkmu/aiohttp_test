import pytest
from main import app


@pytest.fixture
async def client(aiohttp_client):
    client = await aiohttp_client(app)
    return client
