"""Utility for authentication verification"""

from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def login_required(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        if args[0].user.is_authenticated:
            return fun(*args, **kwargs)
        else:
            messages.info(args[0], "Login in required to go further in the site.")
            return redirect("login_user")
    return wrapper
