import json

from core import route, Response


@route('/echo')
def echo(request):
    body = json.dumps({
        'method': request['REQUEST_METHOD'],
        'path': request['PATH_INFO'],
    })
    return Response(body)
