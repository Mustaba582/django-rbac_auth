from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('staff_page/', views.staff_page, name='staff_page'),
    path('member_page/', views.member_page, name='member_page'),
    path('', views.user_login, name='home'), # Default landing page, redirects to login
]
