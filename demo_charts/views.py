from datetime import datetime
import re
import requests
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there!, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)

def stacked_bar(request):
    labels = ['一月','二月','三月','四月','五月']
    datasets = [
        {'label':'資料集 A','data':[10,20,30,40,50]},
        {'label':'資料集 B','data':[5,15,25,35,45]},
        {'label':'資料集 C','data':[2,12,22,32,42]},
    ]
    return render(request, 'demo_list/chart_page.html', {
        'labels': labels,
        'datasets': datasets,
    })
    
@csrf_exempt
def test_api(request):
    if request.method == "POST":
        # 拿到使用者表單送來的水果資料
        name = request.POST.get('name')
        color = request.POST.get('color')

        if name and color:
            # 發送POST到FastAPI
            try:
                res = requests.post('http://localhost:8001/api/v1/fruits/', json={
                    'name': name,
                    'color': color
                })
                res.raise_for_status()
            except requests.RequestException as e:
                print("新增水果失敗", e)

        return redirect('demo_charts:test_api')  # 新增後重新導向自己

    # GET的時候，抓取水果清單
    search = request.GET.get('search', '')
    params = {}
    if search:
        params['search'] = search

    try:
        res = requests.get('http://localhost:8001/api/v1/fruits', params=params)
        res.raise_for_status()
        fruits = res.json()
    except requests.RequestException:
        fruits = []

    return render(request, 'demo_list/demoapi.html', {'fruits': fruits})
