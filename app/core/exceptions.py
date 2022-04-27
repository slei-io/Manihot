from http import HTTPStatus


class SerializerError(Exception):
    def __init__(self, message, status_code=HTTPStatus.BAD_REQUEST):
        super().__init__(message)
        self.status_code = status_code
