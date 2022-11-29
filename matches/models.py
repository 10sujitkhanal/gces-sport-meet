from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _

from players.models import Player
from sports.models import Sports, Team
import uuid

class Session(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    session_year = models.DateField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)


class Organizer(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    organizer_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)



class Tournament(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    tournament_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.tournament_name


class Group(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    group_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)


class Category(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class MatchDate(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    session_year = models.ForeignKey(Session, on_delete= models.CASCADE)
    match_date = models.DateField()
    organizer = models.ForeignKey(
        Organizer,
        verbose_name=_('Organizer'),
        on_delete = models.CASCADE,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

class SingleMatch(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER_CHOICES = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    ]
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    match_date = models.ForeignKey(MatchDate, on_delete=models.CASCADE, null=True)
    sports = models.ForeignKey(Sports, on_delete=models.CASCADE, null=True)
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    description = models.CharField(max_length=255, null=True)
    game_time = models.TimeField(blank=True, null=True)
    is_finish = models.BooleanField(default=False)



# Create your models here.
class Match(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER_CHOICES = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    ]
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    match_date = models.ForeignKey(MatchDate, on_delete=models.CASCADE, null=True)
    sports = models.ForeignKey(Sports, on_delete=models.CASCADE, null=True)
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    team1 = models.ForeignKey(
        Team,
        verbose_name=_('Team 1'),
        on_delete = models.CASCADE,
        related_name = "match_team1"
    )

    team1_score = models.IntegerField(
        verbose_name=_('Score Team 1'), blank=True, null=True
    )

    team2 = models.ForeignKey(
        Team,
        verbose_name=_('Team 2'),
        on_delete = models.CASCADE,
        related_name = "match_team2"
    )

    team2_score = models.IntegerField(
        verbose_name=_('Score away player'), blank=True, null=True)

    tournament = models.ForeignKey(
        Tournament,
        verbose_name=_('Choice a Tournament'),
        on_delete = models.CASCADE
    )

    winner = models.ForeignKey(
        Team,
        verbose_name=_('Team winner'),
        blank=True, null=True,
        on_delete = models.CASCADE,
        related_name = "match_winner_team"
    )

    game_time = models.TimeField(blank=True, null=True)

    category = models.ForeignKey(
        Category,
        help_text=_('Example: playoffs, final, quarter-final'),
        on_delete = models.CASCADE,
    )

    group = models.ForeignKey(
        Group,
        verbose_name=_('Group'), max_length=1,
        help_text=_('Example: A, B, C, D'),
        on_delete = models.CASCADE
    )

    main_image = models.ImageField(
        upload_to='gces/match', blank=True, null=True)

    is_finish = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Match')
        verbose_name_plural = _('Matches')

    def __unicode__(self):
        return "%s %s - %s" % (self.tournament.name, self.team1, self.team2)


# class Standings(models.Model):
#     tournament = models.ForeignKey(
#         Tournament,
#         verbose_name=_('Tournament'),
#         on_delete = models.CASCADE
#     )

#     session_year = models.ForeignKey(Session, on_delete=models.CASCADE)

#     team = models.ForeignKey(
#         Team,
#         verbose_name=_('Team'),
#         on_delete = models.CASCADE
#     )

#     category = models.ForeignKey(
#         Category,
#         help_text=_('Example: playoffs, final, quarter-final'),
#         on_delete = models.CASCADE
#     )

#     group = models.CharField(
#         Group,
#         on_delete = models.CASCADE,
#         help_text=_('Example: A, B, C, D')
#     )


#     # standings table info
#     games_played = models.IntegerField(
#         verbose_name=_("Games Played"), default=0)

#     points = models.IntegerField(
#         verbose_name=_("Points"), default=0)

#     wins = models.IntegerField(
#         verbose_name=_("Wins"), default=0)

#     draws = models.IntegerField(
#         verbose_name=_("Draws"), default=0)

#     losses = models.IntegerField(
#         verbose_name=_("Losses"), default=0)

#     goals_for = models.IntegerField(
#         verbose_name=_("Goals For"), default=0)

#     goals_against = models.IntegerField(
#         verbose_name=_("Goals Against"), default=0)

#     goals_difference = models.IntegerField(
#         verbose_name=_("Goals Difference"), default=0)