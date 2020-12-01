import json

from core import App, Response


@App.route('/')
def echo(request):
    body = json.dumps({
        'method': request['REQUEST_METHOD'],
        'path': request['PATH_INFO'],
    })
    return Response(body)
