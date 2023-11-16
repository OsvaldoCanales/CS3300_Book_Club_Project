from django.http import HttpResponse
from django.shortcuts import redirect 

#This will pass in the list of roles 
def allowed_users(allowed_roles=[]):
    #Pass in view function
    def decorator(view_func):
        #Wrapper function
        def wrapper_func(request, *args, **kwargs):
            #Print and allowed roles
            print('role', allowed_roles)
            group = None
            #if user is part of a group
            if request.user.groups.exists():
                #Grab the first of the list of group
                group = request.user.groups.all()[0].name
            #Checks to see if the group is allowed 
            if group in allowed_roles:
                return view_func(request, * args, **kwargs)
            else: 
                return HttpResponse('You must be authorized to modify this page')
        return wrapper_func
    return decorator
