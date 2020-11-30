import json


def application(request, start_response):
    echo = json.dumps({
        'method': request['REQUEST_METHOD'],
        'path': request['PATH_INFO'],
    })
    start_response('200 OK', [('Content-Type', 'application/json')])
    return [echo.encode()]
