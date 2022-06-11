from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .products import products
from rest_framework.permissions import IsAdminUser, BasePermission, IsAuthenticated
from .models import Product, Customer
from django.contrib.auth.models import User
from .serializer import ProductSerializer, UserSerializer, CustomerSerializer
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from .thread import CreateUserThread, CreateCustomerThread

# Create your views here.


# Simple Token base login..
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    user_id = Token.objects.get(key=token.key).user_id
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user)
    return Response({'token': token.key, "user": serializer.data},
                    status=HTTP_200_OK)

def faker(request):
    # Threading is concept to run operation in the background because some tasks will take more time to complete task that time we can use threading.. 
    count = 500
    CreateUserThread(count).start()
    return HttpResponse('Thread executed successfully..')

def customer_faker(request):
    # Threading is concept to run operation in the background because some tasks will take more time to complete task that time we can use threading.. 
    count = 20
    CreateCustomerThread(count).start()
    return HttpResponse('Thread executed successfully..')

@api_view(['GET'])
def getRoutes(request):
    return Response('Hello')


@api_view(['GET'])
def getUsers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)
    

@api_view(['GET'])
def getProduct(request,pk):
    product = Product.objects.get(_id = pk)
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    data = request.data
    # print(data)
    product = Product.objects.create(
        name = data['name'],
        brand = data['brand'],
        category = data['category'],
        price = data['price']
    )
    serializer = ProductSerializer(product, many=False)
    return Response(200)

@api_view(['PUT'])
def UpdateProduct(request,pk):
    data = request.data
    # print(data)
    product = Product.objects.filter(_id = pk).update(
        name = data['name'],
        brand = data['brand'],
        category = data['category'],
        price = data['price']
    )
    serializer = ProductSerializer(product, many=False)
    return Response(200)

@api_view(['DELETE'])
def DeleteProduct(request, pk):
    order = Product.objects.get(_id=pk)
    order.delete()

    return Response(200)