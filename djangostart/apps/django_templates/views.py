from django.shortcuts import render,HttpResponse,redirect,reverse

# Create your views here.

def index(request):
    kwgs = {
        'protject_name': '超级项目',
        'project_info1': ["超级项目1",'这是一个xxx项目'],
        'project_info2': {'name':"超级项目1",'desc':'这是一个xxx项目2'},
        'good_students': [{'name':'jack', 'hobby':'basketball'},
                          {'name': 'jack', 'hobby': 'basketball'},
                          {'name': 'jack', 'hobby': 'basketball'},
                          {'name': 'jack', 'hobby': 'basketball'},
                          ],
    }
    return render(request, 'django_templates/index.html', kwgs)