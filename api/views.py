
from django.http import JsonResponse, HttpResponse
from api.models import *


def sensor_data(request):
    mac_address = request.GET['m']
    sensor_type = request.GET['t']
    sensor_value = request.GET['v']


    sensor = Sensor( source_mac = mac_address, sensor_type = sensor_type, sensor_value = sensor_value)
    sensor.save();


    data = { 'msg' : 'OK', 'id': sensor.id}
    response = JsonResponse(data, status=200)
    return response

def test (request):
    data = {
        'name': 'John Doe',
        'age' : 30,
        'email' : 'John.doe@example.com'
    }

    response = JsonResponse(data, status=200)
    return response