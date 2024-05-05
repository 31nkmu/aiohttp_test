import asyncio

from tests import client


async def test_healthcheck(client):
    async with client.get('/healthcheck') as response:
        assert response.status == 200
        response = await response.text()
        assert response == '{}'
