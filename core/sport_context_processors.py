from sports.models import Sports, Team
from accounts.models import UserProfile
from players.models import Player

def all_sports(request):
    sports = Sports.objects.all()
    return {'sports':sports} 
