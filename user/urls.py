from django.urls import path

from user import views

urlpatterns = [
    path('', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout_page'),
    path('profile/', views.profile, name='profile'),
]
