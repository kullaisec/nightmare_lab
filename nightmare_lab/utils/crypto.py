import hashlib

def hash_password(pw):
    return hashlib.sha256(("static_salt" + pw).encode()).hexdigest()