from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('', views.main, name='main') # view함수 내부의 main함수를 호출하니까 main함수를 만들고 템플릿과 연결
]
