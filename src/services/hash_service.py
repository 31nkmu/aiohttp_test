import hashlib
import json

from pydantic import ValidationError

from src.common.response.response_schema import response_base
from src.schemas.hash_schema import HashSchema


class HashService:
    @staticmethod
    async def _generate_hash(data) -> str:
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data.encode('utf-8'))
        hash_hex = sha256_hash.hexdigest()
        return hash_hex

    async def get_hash(self, data: json) -> str:
        try:
            hash_obj = HashSchema(**data)
            hash_str = await self._generate_hash(hash_obj.string)
            return response_base.success(data={'hash_string': hash_str})
        except ValidationError as e:
            return response_base.fail(data={'validation_errors': e.json()})


hash_service = HashService()
