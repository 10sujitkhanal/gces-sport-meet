from django.urls import path
from .views import news_detail

urlpatterns = [
    path('<int:id>/<str:uuid>/', news_detail, name='news_detail'),
]
