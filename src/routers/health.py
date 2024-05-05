import json

from aiohttp.web_request import Request
from aiohttp.web_routedef import RouteTableDef

from src.common.response.response_schema import response_base

router = RouteTableDef()


@router.get('/healthcheck')
async def get(request: Request):
    return response_base.success(data={})
