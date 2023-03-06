from django_filters import FilterSet, ModelChoiceFilter, DateFromToRangeFilter
from .models import News, MaterialNews

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class NewsFilter(FilterSet):

   material = ModelChoiceFilter(field_name ='newsmaterial__material',
                                queryset=MaterialNews.objects.all(),
                                label = 'MaterialNews',
                                empty_label = 'любой')
   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = News
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {

           # поиск по названию
           'name': ['icontains'],
           # количество товаров должно быть больше или равно

       }