from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'alfatih', '1883238')
]

username_mapping = {u.username: u for u in users}

user_id_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user
    # User is authenticated


def identety(payload):
    user_id = payload['identity']
    return user_id_mapping.get(user_id, None)
