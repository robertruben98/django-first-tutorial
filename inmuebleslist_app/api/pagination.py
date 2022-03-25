from rest_framework.pagination import PageNumberPagination


class EdificacionPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'p'  # para cambiar el params page por p
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'end'

    # http://127.0.0.1:8000/tienda/edificacion/list/?p=2&size=3
    # http://127.0.0.1:8000/tienda/edificacion/list/?p=end
