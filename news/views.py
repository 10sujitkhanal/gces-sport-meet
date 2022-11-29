from django.shortcuts import render
import datetime

from news.models import News

today = datetime.date.today()

year = today.year
month = today.month
day = today.day

# Create your views here.
def news_detail(request, id, uuid):
    news = News.objects.get(id=id, uuid=uuid)
    today_news = News.objects.filter(is_active=True, create_at__year = year, create_at__month=month, create_at__day=day)
    past_news = News.objects.filter(is_active=True, create_at__lt=today)
    context = {'news': news, 'today_news': today_news, 'past_news':past_news}
    return render(request, 'news/news_detail.html', context)