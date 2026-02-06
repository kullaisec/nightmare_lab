from functools import wraps
from auth.jwt_handler import decode_token

def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token = kwargs.get("token") or ""
        payload = decode_token(token)

        if payload and payload.get("role") != "user":
            return fn(*args, **kwargs)

        return {"error": "unauthorized"}, 401
    return wrapper