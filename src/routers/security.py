from aiohttp.web_request import Request
from aiohttp.web_routedef import RouteTableDef

from src.services.hash_service import hash_service

router = RouteTableDef()


@router.post('/hash')
async def post(request: Request):
    data = await request.json()
    res = await hash_service.get_hash(data)
    return res
