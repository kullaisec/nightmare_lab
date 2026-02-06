from utils.cache import get

def delete_user(uid):
    role = get("role")
    if role == "admin":
        print("User deleted:", uid)