from django.template.loader import get_template
from django.template import Context, RequestContext, TemplateDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
import datetime
import MySQLdb

def hello(request):
    return HttpResponse("Hello World")

def home(request):
    return HttpResponse("Home")

def user_login(request):
    user = {}
    errors = []
    if request.method == 'POST':
        if not request.POST.get('username', ''):
            errors.append('Enter your username !')
        else:
            username = request.POST['username']
        if not request.POST.get('password', ''):
            errors.append('Password required !')
        else:
            password = request.POST['password']

        if not errors:
            user['username'] = username
            user['password'] = password
            return render(request, 'login_success.html', {'user': user})
            # return HttpResponseRedirect('/login/success/')
    return render(request, 'login_form.html', {'errors': errors})

def login_success(request):
    return render(request, 'login_success.html')

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_date.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
    # return render(request, 'current_date.html', {'current_date': now})

def hours_ahead(request, h):
    try:
        offset = int(h)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template('hours_ahead.html')
    html = t.render(Context({'hour_offset': offset, 'next_time': dt}))
    return HttpResponse(html)
    # return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

def display_meta(request):
    values = request.META.items()
    values.sort()
    path = request.path
    host = request.get_host()
    full_path = request.get_full_path()
    secure = request.is_secure()

    t = get_template('meta_table.html')
    html = t.render(Context({
                    'values': values,
                    'path': path,
                    'host': host,
                    'full_path': full_path,
                    'secure': secure,
                    }))

    return HttpResponse(html)
