# django
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
# debug
import pdb  # pdb.set_trace()
# sistema
from datetime import datetime
# utilities
import json

theme = [
    'darkly',
    'sketchy',
    'vapor'
]

links = [
    'https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#user-model',
    'https://ccbv.co.uk/projects/Django/3.2/django.views.generic.base/View/',
    'https://docs.djangoproject.com/es/3.2/'
]

def returnDef():
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    data = {
        'time': now,
        'theme': 'darkly',
        'title': 'Dev',
        'message': '',
        # personalized
    }
    return data

def testReq(req):
    args = req.GET.items()
    # pdb.set_trace()
    # create_user
    data = {
        **returnDef(),
        'message': 'Pagina Dev',
        'links': links
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )
    # return HttpResponse("<a href='https://docs.djangoproject.com/en/3.2/contents/' target='_blank'>Django Doc</a>")

def dev(req, page):
    data = {**returnDef(), 'title': f'{page}', }
    return render(req, f'dev/{page}.html', data)

def numbersSort(req):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    if req.method == 'GET':
        print(now, req.get_host())
        numbers = [int(i) for i in req.GET['numbers'].split(',')]
        sorted_ints = sorted(numbers)
    return

def textFormater(req):
    for post in posts:
        content = ''
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse(content)
