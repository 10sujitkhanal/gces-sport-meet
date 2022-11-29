from django.urls import path
from .views import category_result, result, result_detail, add_team, add_player

urlpatterns = [
    path('<int:id>/<str:uuid>/', category_result, name='category_result'),
    path('result/', result, name='result'),
    path('add_team/', add_team, name='add_team'),
    path('add_player/', add_player, name='add_player'),
    # path('<int:id>/<str:uuid>/result/', result_detail, name='result_detail'),
]
