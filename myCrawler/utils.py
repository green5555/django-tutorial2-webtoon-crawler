import requests
from bs4 import BeautifulSoup

from .models import Episode, Favorite

class Crawler:
    def __init__(self, url, service):
        self.url = url
        self.service = service
        self.selector = self.get_parsing_rule(service)
        self.base_url = self.get_base_url(service)
    
    def crawl(self):
        html = requests.get(self.url).text
        episode_snapshot = BeautifulSoup(html, 'html.parser')

        fetched_list = []
        for episode in episode_snapshot.select(self.selector):
            info = {
                'url' : self.base_url + episode.get('href'),
                'title' : episode.get_text()
            }
            fetched_list.append(info)
        
        return fetched_list
    
    def get_parsing_rule(self, service):
        if service == 'naver' :
            return '#content > table > tr > td.title > a'
        else :
            return ''

    def get_base_url(self, service):
        if service == 'naver' :
            return 'https://comic.naver.com'
        else :
            return ''

