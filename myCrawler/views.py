from django.http import Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
import requests

from .models import Favorite, Episode
from .utils import Crawler

# Create your views here.
def webtoon_index(request):

    if request.method == 'POST' :
        #html에서, submit된 정보들이 request에 실려 들어온다.
        webtoon_title = request.POST.get('webtoon')

        #DB에서 title=webtoon_title로 정의된 Favorite 객체를 찾아온다
        try :
            webtoon = get_object_or_404(Favorite, title=webtoon_title)
        except :
            raise Http404("해당 웹툰이 존재하지 않습니다.")
        
        webtoon_url = webtoon.url
        webtoon_service = webtoon.service
        existing_episode_list = Episode.objects.filter(webtoon=webtoon).order_by('-created_at')
        crawler = Crawler(webtoon_url, webtoon_service)

        #이미 DB에 저장되있는 데이터를 불러와 episodes에 모은다
        episodes = []
        for episode in existing_episode_list:
            e = {
                'title' : episode.title,
                'url' : episode.url
            }
            episodes.append(e)
        
        #전체를 크롤링 해온다
        fetched_episodes = crawler.crawl()

        #DB에 존재하지 않은 데이터들만 모아놓은 result 배열을 만든다
        result = []
        for episode_4_chk in fetched_episodes:
            if episode_4_chk not in episodes:
                result.append(episode_4_chk)
        
        #DB에 result의 데이터를 추가한다.
        for episode in result:
            Episode.objects.create(title=episode['title'], url=episode['url'], webtoon=webtoon)

        return redirect('webtoon_index')

    #when GET
    options = []
    for w in Favorite.objects.all():
        options.append(w.title)

    episode_list = Episode.objects.all()

    data = {
        'options' : options,
        'episode_list' : episode_list
    }

    return render(request, 'myCrawler/webtoon_list_index.html', data)