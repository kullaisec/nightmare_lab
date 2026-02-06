import pickle
from services.admin_service import delete_user

def run(payload):
    obj = pickle.loads(payload)
    if obj.get("action"):
        delete_user(obj["target"])