from django.urls import path

from .views import *

app_name = "card"

urlpatterns = [
    path('get/card/', cards_api, name='cards_api'),

]
