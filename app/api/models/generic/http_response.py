from http import HTTPStatus
from pydantic import BaseModel, Field
from typing import Generic, TypeVar, Optional
from enum import Enum

T = TypeVar('T')


class ResponseType(str, Enum):
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"
    WARNING = "WARNING"

class ApiResponse(BaseModel, Generic[T]):
    status_code: int = Field(..., example=200)
    type: ResponseType = Field(..., example="SUCCESS")
    data: Optional[T] = None
    message: str = Field(..., example="Operación exitosa")
    error_details: Optional[str] = None

def success_response(
    data: Optional[T] = None,
    message: str = "Success",
    status_code: int = HTTPStatus.OK
) -> ApiResponse[T]:
    return ApiResponse[T](
        status_code=status_code,
        type=ResponseType.SUCCESS,
        data=data,
        message=message
    )

def error_response(
    message: str,
    status_code: int = HTTPStatus.BAD_REQUEST,
    error_details: Optional[str] = None
) -> ApiResponse[None]:
    return ApiResponse[None](
        status_code=status_code,
        type=ResponseType.ERROR,
        message=message,
        error_details=error_details
    )