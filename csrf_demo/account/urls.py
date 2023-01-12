from django.urls import path

from .views import login, logout, register, update


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('update/', update, name='update'),
]
