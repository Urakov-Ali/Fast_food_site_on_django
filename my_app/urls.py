from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns  =[
	path('', HomePageView.as_view(), name ='home'),
	path('about/', AboutPageView.as_view(), name ='about'),
	path('menu/', MenuView, name ='menu'),
	path('book/', MessageView, name ='book'),
	path('addfood/', FoodCreateView.as_view(), name ='addFood'),
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)