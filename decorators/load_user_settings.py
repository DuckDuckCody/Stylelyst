from functools import wraps
from flask import request, g
from models.UserSettings import UserSettings

def load_user_settings(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        g.user_settings = UserSettings(request.cookies)
        return f(*args, **kwargs)
    return decorated_function