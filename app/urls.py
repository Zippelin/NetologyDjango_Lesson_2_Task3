from django.urls import path, register_converter
from .views import file_content, file_list
from .converter import DateConverter

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам

register_converter(DateConverter, 'dtc')

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    # path(..., name='file_list'),
    # path(..., name='file_list'),    # задайте необязательный параметр "date"
                                      # для детальной информации смотрите HTML-шаблоны в директории templates
    # path(..., name='file_content'),
    path('', file_list, name='file_list'),
    path('<dtc:date>/', file_list, name='file_list'),
    path('file/<str:name>', file_content, name='file_content'),
]
