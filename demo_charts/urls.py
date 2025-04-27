from django.urls import path
from demo_charts import views
from .views import stacked_bar
app_name = 'demo_charts'
urlpatterns = [
    path('charts/', views.stacked_bar, name='charts_demo'), # /charts/
    path('home', views.home, name='home'),  
    path('hello/<str:name>/', views.hello_there, name='hello_there'),  
    path('testApi/', views.test_api, name='test_api'),  # 也可拉出做獨立app

]