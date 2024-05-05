import json
from typing import Any

from aiohttp.web_response import Response

from src.common.response.response_code import CustomResponseCode, CustomResponse


class ResponseBase:
    @staticmethod
    def __response(*, res: CustomResponseCode | CustomResponse = None, data: Any | None = None) -> Response:
        return Response(status=res.code, text=json.dumps(data))

    def success(
            self,
            *,
            res: CustomResponseCode | CustomResponse = CustomResponseCode.HTTP_200,
            data: Any | None = None,
    ) -> Response:
        return self.__response(res=res, data=data)

    def fail(
            self,
            *,
            res: CustomResponseCode | CustomResponse = CustomResponseCode.HTTP_400,
            data: Any = None,
    ) -> Response:
        return self.__response(res=res, data=data)


response_base = ResponseBase()
