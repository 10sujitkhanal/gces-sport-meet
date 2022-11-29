from django.shortcuts import render
from django.views import View
from accounts.models import UserProfile
from sports.models import Team
from players.models import Player
from matches.models import SingleMatch
# Create your views here.


class RegisterSportPage(View):
    def get(self, request, *args, **kwargs):
        user = UserProfile.objects.get(user=request.user)
        team = Team.objects.filter(batch=user.batch)
        context = {'teams': team}
        return render(request, 'register-player.html', context)


class RegisterSports(View):
    def get(self, request, *args, **kwargs):
        sport = Player.objects.filter(player_name__user=request.user)
        context = {'RegisterSports': sport}
        return render(request, 'register-sports.html', context)


class ClassRegisterSport(View):
    def get(self, request, *args, **kwargs):
        user = UserProfile.objects.get(user=request.user)
        team = Team.objects.filter(batch=user.batch)
        context = {'teams': team}
        return render(request, 'register-player.html', context)

