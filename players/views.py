from django.shortcuts import render
from .models import Player  # Import the Player model

def player_list(request):
    players = Player.objects.all()  # Retrieve all player objects
    return render(request, 'player_list.html', {'players': players})
from django.shortcuts import render, get_object_or_404
from .models import Player

def player_detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render(request, 'player_detail.html', {'player': player})
