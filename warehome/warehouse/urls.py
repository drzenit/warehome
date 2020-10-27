from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('itemPage/<int:pk>/', views.itemView, name='itemView')
]
