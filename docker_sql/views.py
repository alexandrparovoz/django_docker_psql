from django.shortcuts import render
from django.db.models import *

from django.utils import timezone


from .models import *


def index(request):
    return render(request, 'docker_sql/index.html')


def task_1(request):
    clients = Clients.objects.filter(city='Минск').annotate(total=Sum('auto__order__type_service_id__price')).filter(total__lt=500)
    return render(request, 'docker_sql/task_1.html', {'clients': clients})

def task_2(request):
    cities = Order.objects.values('auto_model__client_id__city','date').\
        annotate(total=Sum('type_service_id__price')).filter(date__minute__range=(10, 15)).\
        order_by('-total')
    return render(request, 'docker_sql/task_2.html', {'cities': cities})

def task_3(request):
    autos = Auto.objects.all().annotate(total=Sum('order__type_service_id__price'))
    return render(request, 'docker_sql/task_3.html', {'autos': autos})

def task_4(request):
    services = TypeService.objects.all()
    return render(request, 'docker_sql/task_4.html', {'services': services})

def Orders(request):
    orders = Order.objects.all().annotate(total=Sum('type_service_id__price')).filter(date__minute__range=(10, 15))
    return render(request, 'docker_sql/orders.html', {'orders': orders})


