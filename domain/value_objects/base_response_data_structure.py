from typing import TypedDict


# here we define the structure of the response. All the response data must have the same structure
class ResponseData(TypedDict):
    status_code: int
    message: str
    type_of_response: str
