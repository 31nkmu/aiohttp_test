import hashlib
import json

from tests import client


async def test_hash(client):
    data = {'string': 'Hello, world!'}
    async with client.post('/hash', json=data) as response:
        assert response.status == 200

        json_response = await response.text()
        expected_hash = hashlib.sha256(data['string'].encode()).hexdigest()
        json_response = json.loads(json_response)
        assert json_response['hash_string'] == expected_hash


async def test_hash_no_string_field(client):
    async with client.post('/hash', json={}) as response:

        assert response.status == 400

        json_response = await response.text()
        json_response = json.loads(json_response)
        assert 'validation_errors' in json_response
