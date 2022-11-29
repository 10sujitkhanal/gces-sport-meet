from django.urls import path
from .views import RegisterSportPage, RegisterSports


urlpatterns = [
    path('register-sports', RegisterSportPage.as_view(), name='register-player-page'),
    path('register-profile', RegisterSports.as_view(), name='register-profile'),
]
