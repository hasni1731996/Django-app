from django.conf import settings
from django.shortcuts import render
class CheckUserMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self ,request, view_func, *view_args, **view_kwargs):
        if request.user.is_authenticated:
            print('Yes User Authenticated')
            print('USER EMAIL HERE>>>>>',request.user.email)
            print('USER Role HERE>>>>>>',request.user.user_name.role)
            return view_func(request, *view_args, **view_kwargs)
            
        else:
            print('User Not Authenticated')
            return render(request, '400.html')