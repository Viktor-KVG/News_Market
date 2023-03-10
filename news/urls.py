
from django.urls import path

# Импортируем созданное нами представление
from .views import  NewsCategory, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete


urlpatterns = [
    path('', NewsCategory.as_view()),

   path('<int:pk>', NewsDetail.as_view()),
   path('search/', NewsSearch.as_view(),name='news_search'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete')

]