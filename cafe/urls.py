from django.urls import path
from .views import section_detail, update_section, cafe_view

app_name = 'cafe'

urlpatterns = [
    path('section/<int:section_id>/', section_detail, name='section_detail'),
    path('update_section/<int:section_id>/', update_section, name='update_section'),
    path('', cafe_view, name='index'),  
]
