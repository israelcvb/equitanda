from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('catalog/', views.catalog, name='catalog')
]
