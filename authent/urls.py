from django.urls import path
from authent import views

app_name = 'authUser'

urlpatterns = [
    path('register/', views.registerView, name='register' ),
    path('sign-in/', views.signInView, name='sign-in' ),
    path('log-out/', views.logoutView, name='log-out' ),
]