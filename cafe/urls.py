from django.urls import path
from .views import section_detail, update_section, cafe_view, new_view  # Import the new view

app_name = 'cafe'

urlpatterns = [
    path('section/<int:section_id>/', section_detail, name='section_detail'),
    path('update_section/<int:section_id>/', update_section, name='update_section'),
    path('new.html/', new_view, name='new_view'),  # Add the new path for new_view
    path('', cafe_view, name='index'),
]
