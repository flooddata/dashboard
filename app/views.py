from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Recode
from django.utils import timezone
import plotly.express as px
import plotly.io as pio


def graph_view(request, x,y):
    # Sample data
    data = {'x': x, 'y': y}

    fig = px.line(data, x='x', y='y', title='Simple Plotly Graph')

    # Convert the figure to HTML
    graph_html = pio.to_html(fig, full_html=False)
    return graph_html
    
   # return render(request, 'graph_template.html', {'graph': graph_html})
   

def Home(request):
    # render the page
    # send graph
    graph_html = graph_view(request, [1, 2, 3], [4, 5, 6])
    graph_html2 = graph_view(request, [1, 2, 3], [4, 5, 6])
    graph_html3 = graph_view(request, [1, 2, 3], [4, 5, 6]) 
    graph_html4 = graph_view(request, [1, 2, 3], [4, 5, 6])
    return render(request, 'index.html', {'graph': graph_html, 'graph2': graph_html2, 'graph3': graph_html3, 'graph4': graph_html4})


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


