from django.urls import path
from . import views

app_name = 'api_endpoint'

urlpatterns = [
    path('', views.home, name='home'),
    path('decode_image/', views.decode_image, name='decode_image'),
    path('convert_data_to_image/', views.convert_data_to_image, name='convert_data_to_image'),
]