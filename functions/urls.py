from django.urls import path
from . import views

app_name = "functions"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('image/', views.image, name="image"),
    path('lucky/', views.lucky, name="lucky"),
    path('birthday/', views.birthday, name="birthday"),
    path('ranking/', views.ranking, name="ranking"),
    path('language/<str:name>/', views.language, name="language"),
]