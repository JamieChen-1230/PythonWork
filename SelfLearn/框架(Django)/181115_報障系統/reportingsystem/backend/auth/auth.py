from django.shortcuts import redirect


def check_login(func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('user_info'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/login.html')
    return wrapper
