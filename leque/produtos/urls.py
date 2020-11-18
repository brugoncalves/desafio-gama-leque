from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.find_by_id, name='find_by_id')
]

