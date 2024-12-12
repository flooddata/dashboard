from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Recode
from django.utils import timezone


def Home(request):
    # render the page
    return render(request, 'index.html')


def getSensorData(request):
    # filter temp saved last
    data = Recode.objects.last()
    context = {'data': str(data)}
    return JsonResponse(context, safe=False)


@csrf_exempt
def receiveData(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Check if the token is valid
        token = request.GET.get('token', '')
        if token != 'iot_token':
            return HttpResponse('Invalid token', status=401)

        # Extract the temperature value from the POST request body
        temperature = request.POST.get('temp', '')
        light = request.POST.get('light', '')
        pressure = request.POST.get('pressure', '')
        windD = request.POST.get('windD', '')
        windS = request.POST.get('windS', '')

        if not temperature and light and pressure and windD and windS:
            return HttpResponse('values missing', status=400)

        # Create a new Temperature object and save it to the database
        data_obj = Recode(temp=temperature, light=light, pressure=pressure, windD=windS)
        data_obj.save()

        return HttpResponse('Weather data saved successfully')
    else:
        return HttpResponse('Invalid request method', status=405)

