from django.urls import path

from . import views

app_name = 'barter'

urlpatterns = [
    path('<int:pk>/', views.info, name='info'),
    path('new/', views.new, name='new'),
]