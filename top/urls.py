from top import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('eldete/<int:pk>', views.delete, name='delete'),
    path('edit/<int:pk>', views.edit, name='edit'),
]