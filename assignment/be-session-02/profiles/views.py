from django.shortcuts import get_object_or_404, render
from django.http.response import JsonResponse
import json
from .models import *


def create_introduce(request):
  if request.method == "POST":

    body = json.loads(request.body.decode('utf-8'))

    new_introduce = Introduce.objects.create(
      name     = body['name'],
      major    = body['major'],
      age      = body['age'],
      club     = body['club']
    )

    new_introduce_json = {
      "id"       : new_introduce.id,
      "name"     : new_introduce.name,
      "major"    : new_introduce.major,
      "age"     : new_introduce.age,
      "club"     : new_introduce.club,
    }

    return JsonResponse({
    'status': 200,
    'success': True,
    'message': '생성 성공!',
    'data': new_introduce_json
    })

  return JsonResponse({
    'status': 405,
    'success': False,
    'message': 'method error',
    'data': None
  
  })

def get_introduce(request, id):
  if request.method == "GET":
    introduce = get_object_or_404(Introduce, pk = id)

    introduce_json = {
      "name" : introduce.name,
      "major" : introduce.major,
      "age" : introduce.age,
      "club" : introduce.club,
    }

    return JsonResponse({
      'status' : 200,
      'success' : True,
      'message' : 'introduce 수신 성공',
      'data' : introduce_json
    })

  return JsonResponse({
    'status' : 405,
    'success' : False,
    'message' : 'method error',
    'data' : None
  })