from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import UserInfo

# Create your views here.

# django 会给视图传一个参数(HttpRequest)
def demo01(request):
    """
    :param request:
    :return:
    """
    """
    html = '<h1>i am demo01<h1>'
    print(html)
    # 返回一个HttpResponse对象
    return HttpResponse(html)
    """
    # 参数1固定的，参数2为模块文件，具体可看render源码（最终返回一个HttpResponse对象）
    return render(request, 'app01/templates/app01/demo_01.html')


def demo02(request):
    # print(request.GET)
    # username = request.GET["email"]     # key
    username = request.GET.get("email")
    password = request.GET.get("password")  # get => 当key不存在

    # 返回一个HttpResponse对象
    # request，HTML模板，传递到HTML页面的信息 => 字典格式
    return render(request, 'app01/templates/app01/demo02.html', {"user": username})


def demo02(request):
    # print(request.GET)
    # username = request.GET["email"]     # key
    username = request.GET.get("email")
    password = request.GET.get("password")  # get => 当key不存在

    # 返回一个HttpResponse对象
    # request，HTML模板，传递到HTML页面的信息 => 字典格式
    return render(request, 'app01/templates/app01/demo02.html', {"user": username})


def demo_form2(request):
    """
    post提交
    """
    userlist = {"a@a.com": "123123", "b@b.com": "123123"}
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")  # get => 当key不存在
        # return HttpResponse("<h2>欢迎您，{}</h2>".format(username))
        if username in userlist and password == userlist[username]:
            return HttpResponse("<h2>欢迎您，{}</h2>".format(username))
    # 返回一个HttpResponse对象
    # request，HTML模板，传递到HTML页面的信息 => 字典格式
    # return render(request, 'app01/demo_form2.html')
    return render(request, 'app01/templates/app01/demo_form2.html')


def demo_form_db(request):
    """
    post提交
    """
    # userlist = {"a@a.com":"123123", "b@b.com":"123123"}
    msg = ""
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        result = UserInfo.objects.get(email=username)
        # try...except...
        try:
            if result and result.password == password:
                return HttpResponse("<h2>欢迎您，{}</h2>".format(username))
            else:
                msg = "用户名或密码错误！"
        except:
            pass
    # 返回一个HttpResponse对象
    # request，HTML模板，传递到HTML页面的信息 => 字典格式
    # return render(request, 'app01/demo_form2.html')
    kwgs = {
        "msg":msg,
    }
    return render(request, 'app01/templates/app01/demo_form_db.html', kwgs)