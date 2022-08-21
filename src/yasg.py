from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
	openapi.Info(
		title ="Blog API",
		description ='API project',
		default_version ='v1',
		term_of_service ='',
		contact =openapi.Contact(email ='mukhammadali222@gmail.com'),
		license =openapi.License(name ="Yet we don't have the license"),

	),
	public =True,
	permission_classes =(permissions.AllowAny,),
)

urlpatterns =[
	path('swagger/',schema_view.with_ui(
		'swagger',cache_timeout=0), name ='schema_swagger_ui'),
	path('redoc/',schema_view.with_ui(
		'redoc',cache_timeout=0), name ='schema_redoc'),
]