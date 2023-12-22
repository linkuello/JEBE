from django.urls import path

from . import views

app_name = 'SpecialOffers'

urlpatterns = [
    path('', views.Special_views, name='index'),
]