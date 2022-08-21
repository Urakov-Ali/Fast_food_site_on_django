from django.urls import path
from .views import *

urlpatterns =[
	path('', homeView, name ='home'),
	path('about/', aboutView, name ='about'),
	path('book/', BookView, name ='book'),
	path('menu/', menuView, name ='menu'),
	path('create_product/', ProductCreateView.as_view(), name ='addPro'),
	path('api/menu/',Men.as_view()),
	path('update_item/',updateItem),
	path('cart/',cart, name='cart')
]

