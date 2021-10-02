from django.http import HttpResponse


def page_index_view(request):
    html = "<h1>这是index页面</h1>"
    return HttpResponse(html)


def page_2021_view(request):
    html = "<h1>这是page_2021页面</h1>"
    return HttpResponse(html)


def page_N_view(request, pageNum):
    html = "<h1>这是page %s 页面</h1>" % (pageNum)
    return HttpResponse(html)


def re_view(request, x, op, y):
    html = "<h1>这是re_path页面</h1>"
    return HttpResponse(html)


def request_test_view(request):
    print('path info is', request.path_info)
    print('method is', request.method)
    return HttpResponse("test request ok!")