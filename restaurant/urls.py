#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/menu/', views.MenuItemView.as_view(), name='menu_items'),
    path('api/menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu_item'),
]
