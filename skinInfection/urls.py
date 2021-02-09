from django.http import HttpResponse
from django.urls import path
from skinInfection import views


urlpatterns = [
	path('', views.homepage, name ='home'),
    path('skinInfections', views.skinInfectionDetector, name = 'sid')

]