from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from matches.models import Match, SingleMatch
import datetime

from news.models import News
from sports.models import Sports, Team
from accounts.models import UserProfile
from players.models import Player
from core.models import Student
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

today = datetime.date.today()

year = today.year
month = today.month
day = today.day

class HomePageView(ListView):
    model = Match
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today_news'] = News.objects.filter(is_active=True, create_at__year = year, create_at__month=month, create_at__day=day)
        context['past_news'] = News.objects.filter(is_active=True, create_at__lt=today)
        context['singles'] = SingleMatch.objects.filter(is_finish=False).select_related('sports')
        context['multiples'] = Match.objects.filter(is_finish=False).select_related('sports')
        return context


def category_result(request, id, uuid):
    sports = Sports.objects.get(id=id, uuid=uuid)
    news = News.objects.filter(sports = sports)
    singles =SingleMatch.objects.filter(is_finish=False, sports=sports).select_related('sports')
    multiples = Match.objects.filter(is_finish=False, sports=sports).select_related('sports')
    context = {'news': news, 'sport_name':sports.sport_name, 'singles':singles, 'multiples':multiples}
    return render(request, 'core/results.html', context)


def result(request):
    return render(request, 'result.html')

def result_detail(request, id, uuid):
    return render(request, 'result_detail.html')


def add_team(request):
    if request.user.is_authenticated:
        team_name = request.POST.get('team_name')
        contact = request.POST.get('contact_no')
        user = UserProfile.objects.get(user=request.user)
        team = Team.objects.create(batch=user.batch,team_name=team_name,contact=contact)
        return redirect('/')
    else:
        return redirect('/')

def add_player(request):
    if request.user.is_authenticated:
        print(request.user)
        team_uuid = request.POST.get('team')
        sport_uuid = request.POST.get('sport')
        gender = request.POST.get('gender')
        user = UserProfile.objects.get(user=request.user)
        team = Team.objects.get(uuid=team_uuid)
        student = Student.objects.get(user=request.user)
        sport = Sports.objects.get(uuid=sport_uuid)
        from django.core.exceptions import ValidationError
        player_single_game = Player.objects.filter(player_name__user = request.user, sport=sport).count()
        player_register = Player.objects.filter(player_name__user=request.user, sport=sport).count()

        player_count_football = Player.objects.filter(sport__sport_name= "Football", team = team).count()
        player_count_volleyball = Player.objects.filter(sport__sport_name= "Volleyball", team = team).count()
        player_count_tableteniss = Player.objects.filter(sport__sport_name= "Table Tennis (Double)", team = team).count()
        player_count_badminton = Player.objects.filter(sport__sport_name= "Badminton (Double)", team = team).count()
        player_count_cricket = Player.objects.filter(sport__sport_name= "Cricket", team = team).count()



        if(player_single_game > 4):
            messages.error(request, 'Player cannot participate in more than 3 single game')
            return redirect('/register-sports')
        elif player_register > 0:
            messages.error(request, 'Already in the team')
            return redirect('/register-sports')
        
        elif(player_count_tableteniss >= 2):
            messages.error(request, 'Player already fulfilled')
            return redirect('/register-sports')
        
        elif(player_count_badminton > 2):
            messages.error(request, 'Player already fulfilled')
            return redirect('/register-sports')

        elif player_count_football >= 11:
            messages.error(request, 'Player already fulfilled')
            return redirect('/register-sports')
        
        elif player_count_cricket >= 8:
            messages.error(request, 'Player already fulfilled')
            return redirect('/register-sports')
        
        elif player_count_volleyball >= 9:
            messages.error(request, 'Player already fulfilled')
            return redirect('/register-sports')
        else:
            team = Player.objects.create(team=team,player_name=student,sport=sport, gender=gender)
            messages.success(request, 'Player register success')

            return redirect('/register-sports')
    else:
        return redirect('/')