from django.shortcuts import render

from  urllib.request import urlopen
from urllib.error import HTTPError
from django.http import HttpResponse

import json
# Create your views here.
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def check(request):
    lol = json.dumps(request.POST)
    data = json.loads(lol)
    try:
        #urlopen(new_link.url)
        urlopen(data['url'])
        print("I am an awesome Checker")
        return HttpResponse(status = 200, content_type = None)
    except HTTPError as e_x:
        print("I am checker And I couldn't find the links "+str(e_x))
        return HttpResponse(status = 400, content_type = None)