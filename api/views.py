from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def test (request):
    data = {
        'name': 'John Doe',
        'age' : 30,
        'email' : 'John.doe@example.com'
    }

    response = JsonResponse(data, status=200)
    return response
