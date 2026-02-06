import jwt
from config import SECRET

def decode_token(token):
    try:
        return jwt.decode(token, SECRET, options={"verify_signature": False})
    except:
        return None