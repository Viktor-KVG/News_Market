
from django.urls import path

# Импортируем созданное нами представление
from .views import  NewsCategory, NewsDetail


urlpatterns = [
    path('', NewsCategory.as_view()),

   path('<int:pk>', NewsDetail.as_view())

]