from django.http import HttpResponse


def page_2021_view(request):
    html = "<h1>这是page_2021页面</h1>"
    return HttpResponse(html)