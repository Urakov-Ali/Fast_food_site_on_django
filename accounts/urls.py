from django.urls import path
from .views import LoginCreateView

urlpatterns =[
	path('signup/', LoginCreateView.as_view(), name='signup')
	]