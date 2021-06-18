from news import views
from django.conf.urls import url

urlpatterns = [
    # http://localhost:8000/news/articles
    url(r'articles', views.index, name='index'),
    # http://localhost:8000/news/articles/5
    url(r'articles/<int:year>', views.year_archive, name='year_archive'),

    url(r'articles/<int:year>/<int:month>', views.month_archive, name='month_archive'),

    url(r'articles/<int:year>/<int:month>/<int:pk>', views.article_archive, name='article_archive'),
]

