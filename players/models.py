from django.db import models
import uuid

from sports.models import Position, Sports, Team
from core.models import Student
# Create your models here.
GENDER_CHOICE = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class Player(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_name = models.ForeignKey(Student, on_delete = models.CASCADE)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, null=True)
    sport = models.ForeignKey(Sports, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.player_name.student_name

    def clean(self):
        from django.core.exceptions import ValidationError

        player_count_football = Player.objects.filter(sport__sport_name= "Football", team = self.team).count()
        player_count_volleyball = Player.objects.filter(sport__sport_name= "Volleyball", team = self.team).count()
        player_count_tableteniss = Player.objects.filter(sport__sport_name= "Table Tennis (Double)", team = self.team).count()
        player_count_badminton = Player.objects.filter(sport__sport_name= "Badminton (Double)", team = self.team).count()
        
        if(player_count_tableteniss >= 2):
            raise ValidationError('Player already fulfilled')
        
        if(player_count_badminton > 2):
            raise ValidationError('Player already fulfilled')

        if player_count_football >= 11:
            raise ValidationError('Player already fulfilled')
        
        player_count_cricket = Player.objects.filter(sport__sport_name= "Cricket", team = self.team).count()
        if player_count_cricket >= 8:
            raise ValidationError('Player already fulfilled')
        
        if player_count_volleyball >= 9:
            raise ValidationError('Player already fulfilled')
        


class PlayerInfo(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete = models.CASCADE)
    player_goal = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)