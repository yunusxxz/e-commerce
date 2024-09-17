from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product_list'),
    path('<int:product_id>/', views.detail, name='product_detail')
]
