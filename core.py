from json import dumps
from http.client import responses


class Response:

    def __init__(
            self,
            text: str = '',
            json: dict = None,
            status: int = 200,
            headers: dict = None
    ):
        if json:
            self.body = dumps(json)
            content_type = 'text/json'
        else:
            self.body = text
            content_type = 'text/plain'

        self.status = status

        resp_headers = {
            'Content-Type': content_type
        }
        if headers:
            resp_headers.update(headers)

        self.headers = list(resp_headers.items())


def route(path: str) -> callable:
    def wrapper(func):
        App.add_handler(path, func)
        return func

    return wrapper


def not_found_handler(request: dict) -> Response:
    return Response(text='Not found :(', status=404)


def redirect_handler(request: dict) -> Response:
    location = request['PATH_INFO'][:-1]
    return Response(status=301, headers={'Location': location})


class App:
    _handlers = {}

    def __call__(self, request: dict, start_response: callable) -> list:
        path = request['PATH_INFO']
        handler = self._handlers.get(path, not_found_handler) if path.endswith('/') else redirect_handler
        resp = handler(request)

        start_response(
            f'{resp.status} {responses[resp.status]}',
            resp.headers
        )
        return [resp.body.encode()]

    @classmethod
    def add_handler(cls, path: str, handler: callable) -> None:
        cls._handlers[path] = handler
