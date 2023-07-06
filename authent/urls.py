from django.urls import path
from authent import views

app_name = 'authUser'

urlpatterns = [
    path('register/', views.registerView,name='register' )
]