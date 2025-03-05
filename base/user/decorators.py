from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(view_func):
    """
    Decorator to redirect authenticated users to their respective profile pages.
    If the user is a company, they are redirected to the company profile page.
    If the user is an applicant, they are redirected to the applicant feed.
    If the user is not authenticated, the original view function is called.
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_company:
            return redirect('company-profile', request.user.id)
        elif request.user.is_authenticated and request.user.is_applicant:
            return redirect('applicant-feed')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def show_to_applicant(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_admin or request.user.is_applicant:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")

        return wrapper_func

    return decorator


def show_to_company(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_admin or request.user.is_company:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")

        return wrapper_func

    return decorator
