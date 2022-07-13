from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .tests import telegram_bot_send_message
from .models import Food, Messages
from django.core.paginator import Paginator
import requests
from django.urls import reverse_lazy

class HomePageView(ListView):
	model =Food
	template_name ='home.html'

class AboutPageView(TemplateView):
	template_name ='about.html'

# class MenuPageView(ListView):
# 	model =Food
# 	template_name ='menu.html'

class BookPageView(ListView):
	model =Food
	template_name ='book.html'


def MenuView(request):
	obj =Food.objects.all()
	page_n =request.GET.get('page', 1)
	p =Paginator(obj,3)
	try:
		page =p.page(page_n)
	except Exception:
		page =p.page(1)
	context ={
	'page':page
	}
	return render(request, 'menu.html',context)

def MessageView(request):
	if request.method == 'POST':
		Name =request.POST.get('Name', None)
		Number =request.POST.get('Number', None)
		Email =request.POST.get('Email', None)
		Message =request.POST.get('Message', None)
		user =Messages.objects.create(
			Name =Name,
			Number =Number,
			Email =Email,
			Message =Message
			)
		user.save()
		telegram_bot_send_message(f"Ismi: {Name} \nTel raqam: {Number} \nE-mail: {Email} \nMijoz fikri: {Message}")

	return render( request =request, template_name ='book.html' )


class FoodCreateView(CreateView):
	model =Food
	template_name ='addFood.html'
	fields ='__all__'
	success_url =reverse_lazy('home')