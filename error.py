#
# Code by Francesco Pallara
#

import re


class ClasseVivaHTTPError(Exception):

    def __init__(self, message: str, status_code: int):
        super().__init__()

        self.status_code = status_code

        message = message.removeprefix("252:CvvRestApi/")

        self.message = message.capitalize()

    def __str__(self) -> str:
        return f"{self.message} [{self.status_code}]"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.message}')"
