from django import template


register = template.Library()


list_words = {
   'начале': 'н*****',
   'секрет': 'с*****',
}


@register.filter()
def censor(text):
   """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """

   text = list_words.values()
   if list_words.keys() == True:
       return text



