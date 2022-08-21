from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import *
from django.core.paginator import Paginator
from .tests import telegram_bot_send_message
from django.urls import reverse_lazy
import requests
from rest_framework.generics import ListAPIView
from .serializers import menuSerializers
from django.http import JsonResponse
import json


class Men(ListAPIView):
	queryset =Menu.objects.all()
	serializer_class =menuSerializers


def homeView(request):
	if request.user.is_authenticated:
		model =Menu.objects.all()
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items # Savatdagi mahsulot nomi
		context = {
		'object_list':model,
		'cartItems':cartItems
		}
		return render(request,'home.html',context)
	else:
		model =Menu.objects.all()
		items = []
		order = {'get_cart_total': 0, "get_cart_items": 0}
		cartItems = order['get_cart_items']
		context = {
		'object_list':model,
		'cartItems':cartItems
		}
		return render(request,'home.html',context)

def aboutView(request):
	if request.user.is_authenticated:
		model =Menu.objects.all()
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items # Savatdagi mahsulot nomi
		context = {
		'object_list':model,
		'cartItems':cartItems
		}
		return render(request,'about.html',context)
	else:
		model =Menu.objects.all()
		items = []
		order = {'get_cart_total': 0, "get_cart_items": 0}
		cartItems = order['get_cart_items']
		context = {
		'object_list':model,
		'cartItems':cartItems
		}
		return render(request,'about.html',context)


def menuView(request):
	if request.user.is_authenticated:
		customer =request.user 
		print(request.user)
		order, created =Order.objects.get_or_create(customer=customer, complete =False)
		items  =order.orderitem_set.all()
		cartItems =order.get_cart_items #the number of products in bin
	else:
		items =[]
		order ={'get_cart_total':0, 'get_cart_items':0}
		cartItems =order['get_cart_items'] #by which function it should calculate

	obj = Menu.objects.all()
	page_n = request.GET.get('page',1)
	p = Paginator(obj,3)
	try:
			page = p.page(page_n)
	except Exception:
			page = p.page(1)
	context = {
		'page' : page,
		'cartItems': cartItems
	}
	return render(request, 'menu.html',context)

def BookView(request):
	if request.method == 'POST':
		name =request.POST.get('name', None)
		phone =request.POST.get('phone', None)
		email =request.POST.get('email', None)
		message =request.POST.get('message', None)
		user =Comment.objects.create(
			userName =name,
			phone =phone,
			email =email,
			message =message
			)
		user.save()
		telegram_bot_send_message(f"Ismi: {user} \nTel raqam: {phone} \nE-mail: {email} \nMijoz fikri: {message}")

	return render(request,'book.html')

class ProductCreateView(CreateView):
	model =Menu
	template_name ='addPro.html'
	fields ='__all__'
	success_url =reverse_lazy('home')

#We will write a function to add the prodcuts
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Clicked: ',action) #This to see the ID of the product on Terminal
	print("Product's ID: ",productId)

	# The next changing is creating the Post
	# We need to show the quantity of the product on the icon on base.html
	customer = request.user
	product = Menu.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer,complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)
	elif action == 'delete':
		orderItem.quantity = 0
	
	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)
	# we need to make a url for this function


# function for cart.html
def cart(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		# reverse_lazy('login')
		items = []
		order = {'get_cart_total': 0, "get_cart_items": 0}
		cartItems = order['get_cart_items']

	context = {"items": items,"order": order,'cartItems':cartItems }
	return render(request, 'cart.html', context)
	# we need to make a url for this function
	# wee need to mark the cart on the url of the bin on base.html


















