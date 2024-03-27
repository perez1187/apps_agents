from rest_framework.pagination import PageNumberPagination

class NicknamePagination(PageNumberPagination):
    # Returns 10 elements per page, and the page query param is named "page_no"
    page_size = 100
    page_query_param = 'page_no'