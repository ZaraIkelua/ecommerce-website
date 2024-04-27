"""Utility for authentication verification"""

from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def login_required(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        if args[0].user.is_authenticated and not args[0].user.is_superuser:
            return fun(*args, **kwargs)
        else:
            messages.info(args[0], "Login in required to go further in the site.")
            return redirect("signin")
    return wrapper
