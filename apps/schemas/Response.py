from pydantic import BaseModel
from typing import List


class BaseResponse(BaseModel):
    status: int = 200
    message: str = None
    data: List = []