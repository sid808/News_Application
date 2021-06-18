from news import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    # http://localhost:8000/news/articles
    path(r'articles', views.index, name='index'),
    # http://localhost:8000/news/articles/5
    path(r'articles/<int:year>', views.year_archive, name='year_archive'),
    
    path(r'articles/<int:year>/<str:month>', views.month_archive, name='month_archive'),

    path(r'articles/<int:year>/<str:month>/<int:pk>', views.article_archive, name='article_archive'),
]

