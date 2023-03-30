from datetime import datetime
from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.db.models import Sum
from .models import *

def home(request) :
    return render(request, 'homepage1.html')

def index(request):
    tables = Table.objects.all().order_by('number')
    meals = Meal.objects.filter(end=None).order_by('table')
    id_open_table= set([p.table.number for p in meals])
    tables_available= []
    for t in tables:
        if t.number not in id_open_table:
            tables_available.append(t)
    return render(request, 'home.html', {'table_available': tables_available, 'meal': meals})

def createNewOrder(request,number):
    if request.method == 'POST':
        clicked_dish_id =request.POST.get('dishes')
        dish = Dish.objects.filter(id=clicked_dish_id).first()
        new_order= Order(request_time=datetime.now(), dish_name= dish, table=number)
        new_order.save()

def open(request, number):
    tav = Table.objects.get(number = number)
    if Meal.objects.filter(table=tav).exists():
        print("esiste")
    else :
        p = Meal(table=tav, start=datetime.now())
        p.save()
    dishes = Dish.objects.all().order_by('type')
    createNewOrder(request,tav)
    return render(request, 'nuovo.html', {'dishes': dishes, 'table': tav})


def kitchen(request):
    orders = Order.objects.filter(kitchen_end_time=None).order_by('request_time')
    return render(request, 'cucina.html', {'orders': orders})

#comando cottura
def cookingStarted(request,id):
    Order.objects.filter(id=id).update(kitchen_start_time=datetime.now())
    return HttpResponseRedirect('/kitchen/')

def cookingEnded(request,id):
    Order.objects.filter(id=id).update(kitchen_end_time=datetime.now())
    return HttpResponseRedirect('/kitchen/')

def showOrderstoDeliver(request):
    openOrders = Order.objects.filter(delivery_time__isnull=True).order_by('table')
    return render( request,'Incorso.html', {'orders':openOrders})

def closeOrder(request,id):
    Order.objects.filter(id=id).update(delivery_time=datetime.now())
    return HttpResponseRedirect('/openOrders/')

def cashierPage(request):
    tables = Meal.objects.filter(end=None).order_by('table')
    return render(request, 'cassa.html', {'tables': tables})

def pay(request,tNumber):
    dishesOrdered=Order.objects.filter(table=tNumber).select_related('dish_name')
    costList=[]
    for d in dishesOrdered:
     val=d.dish_name
     x= Dish.objects.filter(name=val).values_list('price', flat=True)[0]
     costList.append(x)   
    b=sum(costList)    
    Meal.objects.filter(table=tNumber).update(end=datetime.now())

    return render(request, 'bill.html', {'dishesOrdered': dishesOrdered, 'b':b, 'table':tNumber})

def clearTable(request, tNumber):
    Order.objects.filter(table=tNumber).delete()
    Meal.objects.filter(table=tNumber).delete()
    return HttpResponseRedirect('/home/')
