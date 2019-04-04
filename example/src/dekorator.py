from functools import wraps

from flask import Flask, request, Response

app = Flask(__name__)


def requires_authentication(f):
    @wraps(f)
    def decorated():
        auth = request.headers.get('Authorization')
        if not auth or auth != 'Bearer my-secret-api-key':
            return Response('Not Authorized', 401, {'WWW-Authenticate': 'Bearer realm="Bearer"'})
        return f()

    return decorated


@app.route('/')
@requires_authentication
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()

# def may_authenticate(check=True):
#     def check_auth(f):
#         @wraps(f)
#         def authenticate():
#             if not check:
#                 return f()
#             auth = request.headers.get('Authorization')
#             if not auth or auth != 'Bearer my-secret-api-key':
#                 return Response('Not Authorized', 401, {'WWW-Authenticate': 'Bearer realm="Bearer"'})
#             return f()
#
#         return authenticate
#
#     return check_auth
