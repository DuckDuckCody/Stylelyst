from functools import wraps
from flask import request
from models import UserSettings

def load_user_settings(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        request.user_settings = UserSettings(request.cookies)
        return f(*args, **kwargs)
    return decorated_function