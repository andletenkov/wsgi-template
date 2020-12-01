from dataclasses import dataclass, field


@dataclass
class Response:
    body: str
    status_code: str = '200 OK'
    headers: list = field(default_factory=list)


def not_found_handler(*args, **kwargs) -> Response:
    return Response('Not found :(', '404 Not Found', [('Content-Type', 'text/plain')])


class App:
    _handlers = {}

    def __call__(self, request: dict, start_response: callable) -> list:
        path = request['PATH_INFO']
        handler = self._handlers.get(path, not_found_handler)
        response = handler(request)

        start_response(response.status_code, response.headers)
        return [response.body.encode()]

    @classmethod
    def add_handler(cls, route: str, handler: callable) -> None:
        cls._handlers[route] = handler

    @classmethod
    def route(cls, path: str) -> callable:
        def wrapper(func):
            cls.add_handler(path, func)
            return func

        return wrapper
