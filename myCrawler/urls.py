from django.urls import path
from .views import webtoon_index

urlpatterns = [
    path('', webtoon_index, name='webtoon_index')
]