def application(environ, start_response):
    start_response("200 OK", ["Content-Type", "application/json"])
    return '{"msg": "new hello world"}'
