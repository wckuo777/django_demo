from django.shortcuts import render

def index(request):
    # return render(request, 'index.html')
    apps = [
        {'name': '圖表範例', 'url': '/charts/'},
        {'name': '範例API', 'url': '/testApi/'}
    ]
    return render(request, 'index.html', {'apps': apps})
