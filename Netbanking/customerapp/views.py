from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from customerapp.models import Customer

# Create your views here.
def index(request):
    content = "<h2> Hello, world. This is CustomerApp!!!</h2><br><br>"
    content = content + "<a href='all_customer/'>All Customer</a> <br><br>" 
    content = content + "<a href='add_customer/'>Add Customer</a> <br><br>" 
    return HttpResponse(content)

def all_customer(request):
    latest_customer_list = Customer.objects.all()
    context = {
        'latest_customer_list': latest_customer_list
    }
    return render(request, 'customerapp/customerlist.html', context)

def detail(request, customer_id):
    customer = get_object_or_404(Customer,pk=customer_id)
    context = {
        'customer': customer
    }
    return render(request, 'customerapp/customerdetails.html',context)

def add_customer(request):
    return render(request, 'customerapp/addcustomer.html')

from django.utils import timezone
def add(request):
    name = request.POST['name']
    account = request.POST['account']
    balance = request.POST['balance']
    address = request.POST['address']


    customer = Customer(name=name, account=account, balance=balance, address=address, pub_date=timezone.now())

    message = ""

    try:
        customer.save()
        message = "customer data submitted SUCCESSFULLY!!!!"
    except:
        message = "Can't save customer details ,please try again"
    context = {'message':message}
    return render(request, 'customerapp/addcustomer.html', context)

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer,pk=customer_id)
    message = ""
    try:
        customer.delete()
        message = "customer data deleted."
    except:
        message = ("Can't delete customer details. try again")
    message = message + "<br><br><a href='../../all_customer/'>Back</a>"
    #context = {'message':message}
    return HttpResponse(message)

# from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Customer
from .serializers import CustomerSerializer

@csrf_exempt
def customer_list(request):

    if request.method == 'GET':
        customers=Customer.objects.all()
        serializer=CustomerSerializer(customers,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        print(request.body) 
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
         
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors,status=404)

@csrf_exempt
def customer_detail(request, pk):
    try:
        customer=Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        print(request.body) 
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(customer,data=data)
         
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors,status=404)

    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse("customer record delete succesfully ",status=200)
