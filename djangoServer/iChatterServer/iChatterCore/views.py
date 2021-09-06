from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,Http404,HttpResponseBadRequest

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status


import json


@csrf_exempt
def jarvis_version(request):

    if(request.method == 'POST'):

        key = str(request.POST["key"])

        if(key == "2D5fCt9wW1UmwjBf"):
            response = json.dumps([{'version':0.1}])
            return HttpResponse(response , content_type='text/json')
        else:
            return HttpResponseBadRequest("invalid key")
            
    
    else:
        return HttpResponseBadRequest("API only available via POST method")

