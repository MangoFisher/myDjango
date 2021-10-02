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


def test_get_post_view(request):
    if request.method == 'GET':
        print(request.GET['a'])
        print(request.GET.get('c', 'no c exist!!!'))
    elif request.method == 'POST':
        pass
    else:
        pass
    return HttpResponse("in test_get_post_view")


#测试django的模版功能
def test_html_view(request):
    #开始：模版的加载方式一
    # from django.template import loader
    # t = loader.get_template("test_html.html")
    # html = t.render()
    # return HttpResponse(html)
    #结束：模版的加载方式一

    #开始：模版的加载方式二
    from django.shortcuts import render
    return render(request, "test_html.html")
    #结束：模版的加载方式二