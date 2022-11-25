from django.shortcuts import render

from apps.card.models import *


def cards_api(request):
    user_id = request.POST.get('user_id')
    cards = Card.objects.filter(user_id=user_id)
    context = {
        'cards': cards,
    }
    return render(request, "apps/cards/get_cards_api.html", context)
