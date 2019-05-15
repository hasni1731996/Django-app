from django.shortcuts import render

def check_user(view_func):
    def decorator(request,*args,**kwargs):
        if request.user.is_authenticated:
            print('USER EMAIL HERE>>>>>',request.user.email)
            print('USER Role HERE>>>>>>',request.user.user_name.role)
            return view_func(request,*args,**kwargs)
            
        else:
            print('User Not Authenticated')
            return render(request, '400.html')
    return decorator
    