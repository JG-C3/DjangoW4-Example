from django.urls import path
from . import views

# [코드 작성] 'functions'앱 이름 설정하기
app_name = "functions"

# 'path'의 'name' 속성으로 url의 별칭을 지정하기
urlpatterns = [
    path('index/', views.index, name="index"),
    path('image/', views.image, name="image"),
    path('lucky/', views.lucky, name="lucky"),
    path('birthday/', views.birthday, name="birthday"),
    path('ranking/', views.ranking, name="ranking"),
    # [코드 작성] 문자열 인자 전달하기
    path('language/<str:name>/', views.language, name="language"),
]