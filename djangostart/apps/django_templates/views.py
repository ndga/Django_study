from django.shortcuts import render,HttpResponse,redirect,reverse

# Create your views here.

def index(request):
    kwgs = {
        'protject_name': '超级项目',
        'project_info1': ["超级项目1",'这是一个xxx项目'],
        'project_info2': {'name':"超级项目2",'desc':'这是一个xxx项目2'},
        'good_students': [{'name':'j', 'hobby':'basket'},
                          {'name': 'ja', 'hobby': 'basketb'},
                          {'name': 'jac', 'hobby': 'basketba'},
                          {'name': 'jack', 'hobby': 'basketball'},
                          ],
        # 'good_students':[]
        'title':'<h1>这是一级标题</h1>'
    }
    return render(request, 'django_templates/index.html', kwgs)