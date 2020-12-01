from core import route, Response


@route('/echo')
def echo(request):
    body = {
        'method': request['REQUEST_METHOD'],
        'path': request['PATH_INFO'],
    }
    return Response(json=body)
