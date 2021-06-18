# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the news index.")


def year_archive(request, year):
    # a_list = Article.objects.filter(pub_date__year=year)
    # context = {'year': year, 'article_list': a_list}
    # return render(request, 'news/year_archive.html', context)
    return HttpResponse("Hello, world. You are at the %s YEAR archieve." % year)


def month_archive(request, year, month):

    return HttpResponse("Hello, world. You are at the %s YEAR %s MONTH archieve." % (year, month))


def article_archive(request, year, month, pk):

    return HttpResponse("Hello, world. You are at the %s YEAR %s MONTH ARCHIVE: %s." % (year, month, pk))
