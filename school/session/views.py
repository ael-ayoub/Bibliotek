from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.backends.db import SessionStore
# Create your views here.
def get_views(request):
    # visits = request.session.get('visits',0)
    # request.session['key1'] = 33
    # request.session['key2'] = 333333
    # key = request.session.session_key
    # visits += 1
    # request
    # request.session['key1'] = 2223333333

    key_id = request.session.session_key
    a = SessionStore(session_key=key_id)
    # a.update('key1')
    a['key1'] = 22222222
    a.save()
    data = a.load()
    response  = f"{data}"
    # request.session['visits'] = visits
    # response = f"this is session_key \'{key}\'"
    # return HttpResponse(f"You visit this page: {visits} times")
    
    return HttpResponse(response)