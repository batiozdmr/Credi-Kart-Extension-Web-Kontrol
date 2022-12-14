from django.urls import path

from .views import *

app_name = "api"

urlpatterns = [
    path('login_control/', login_control, name='login_control'),
    path('login_control_login/', login_control_login, name='login_control_login'),
    path('cardData/', cardData, name='cardData'),
    path('userData/', userData, name='userData'),
    path('card-detail/', cardDetail, name='cardDetail'),
    path('card-update/', cardUpdate, name='cardUpdate'),
    path('card-add/', cardAdd, name='cardAdd'),
    path('card-delete/', cardDelete, name='cardDelete'),
]
