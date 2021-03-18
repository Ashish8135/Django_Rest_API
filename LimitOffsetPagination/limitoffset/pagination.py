from rest_framework.pagination import LimitOffsetPagination

class MyLimitPagination(LimitOffsetPagination):
    default_limit=5
    limit_query_param='limit'
    offset_query_param='myoffset'
    max_limit=4