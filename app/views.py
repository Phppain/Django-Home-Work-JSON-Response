from django.shortcuts import render
from django.http import JsonResponse
from random import randint

def returnJSON(request):
    data = {i: randint(1, 99999) for i in range(randint(1, 99999))}
    return JsonResponse(data)
