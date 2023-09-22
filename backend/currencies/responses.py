import json
from typing import Dict, Tuple

from domain.value_objects.base_response_data_structure import ResponseData


DictResponse = Dict[str, Dict[str, str | int]]


class Response:
    def __init__(self, response_data: ResponseData) -> None:
        self.response_data = response_data

    def _validate_type_of_response(self) -> None:
        if not self.response_data["type_of_response"] or self.response_data[
            "type_of_response"
        ] not in [
            "success",
            "error",
        ]:
            raise Exception("Invalid type of response.")

    def _response_as_dictionary(self) -> DictResponse:
        # form of dictionary: {"success": {"message": message, "status_code": status_code}}
        return {
            self.response_data["type_of_response"]: {
                "message": self.response_data["message"],
                "status_code": self.response_data["status_code"],
            }
        }

    def build_response(self) -> Tuple[str, int]:
        self._validate_type_of_response()
        return (
            json.dumps(self._response_as_dictionary()),
            self.response_data["status_code"],
        )
