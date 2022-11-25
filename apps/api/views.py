import hashlib

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render

from apps.card.models import *


def login_control(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    user_cont = User.objects.get(email=email)
    if not user_cont.check_password(password):
        data = "Başarılı"
        login(request, user_cont, backend='django.contrib.auth.backends.ModelBackend')
    else:
        data = "Başarısız"
    context = {
        'data': data,
    }
    return render(request, "apps/api/data.html", context)


def login_control_login(request):
    if request.user:
        email = request.user.email
        password = request.user.password
        statu = "Başarılı"
        data = str(statu) + "{//}" + str(email) + "{//}" + str(password)
    else:
        statu = "Başarısız"
        data = str(statu)
    context = {
        'data': data,
    }
    return render(request, "apps/api/data.html", context)


def cardData(request):
    card_list = Card.objects.filter()
    context = {
        'card_list': card_list,
    }
    return render(request, "apps/api/card_list_api.html", context)


def cardDetail(request):
    id = request.GET.get('id')
    card = Card.objects.filter(id=id).first()
    context = {
        'card': card,
    }
    return render(request, "apps/api/card_detail_api.html", context)


def cardUpdate(request):
    statu = "False"
    id = request.GET.get('id')
    number = request.GET.get('number')
    name = request.GET.get('name')
    expiry = request.GET.get('expiry')
    cvc = request.GET.get('cvc')
    card = Card.objects.filter(id=id).update(number=number,
                                             name=name,
                                             expiry=expiry,
                                             cvc=cvc
                                             )
    if card:
        statu = "True"
    context = {
        'data': statu,
    }
    return render(request, "apps/api/data.html", context)


def cardAdd(request):
    statu = "False"
    number = request.GET.get('number')
    name = request.GET.get('name')
    expiry = request.GET.get('expiry')
    cvc = request.GET.get('cvc')
    card = Card.objects.create(number=number,
                               name=name,
                               expiry=expiry,
                               cvc=cvc
                               )
    if card:
        statu = "True"
    context = {
        'data': statu,
    }
    return render(request, "apps/api/data.html", context)


def userData(request):
    return render(request, "apps/api/user_index_api.html")


def cardDelete(request):
    statu = "False"
    id = request.GET.get('id')
    card = Card.objects.filter(id=id).delete()
    if card:
        statu = "True"
    context = {
        'data': statu,
    }
    return render(request, "apps/api/data.html")
