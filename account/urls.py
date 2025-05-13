from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('verify/', views.verify_code_view, name='verify_code'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account_view, name='account'),
    path('account/change-password/', views.change_password_view, name='change_password'),
    path('update/', views.profile_update, name='profile_update'),
]
