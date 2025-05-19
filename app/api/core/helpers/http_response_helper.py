from http import HTTPStatus
from typing import Optional
from fastapi.responses import JSONResponse

from app.api.models.generic.http_response import T, GenericResponse, ResponseType

def create_response(
    data: Optional[T] = None,
    message: str = "",
    response_type: ResponseType = ResponseType.SUCCESS,
    status_code: int = HTTPStatus.OK
) -> GenericResponse[T]:
    return GenericResponse[T](
        code=status_code,
        response_type=response_type,
        data=data,
        message=message
    )