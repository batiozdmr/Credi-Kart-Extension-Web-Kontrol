from django.shortcuts import render

from apps.card.models import *


def cards_api(request):
    cards = Card.objects.filter()
    context = {
        'cards': cards,
    }
    return render(request, "apps/cards/get_cards_api.html", context)
